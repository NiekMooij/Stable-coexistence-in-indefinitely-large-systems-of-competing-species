import networkx as nx
import numpy as np
from scipy.integrate import ode
import random
import os
import sys
import warnings
import pickle
    
def LV_integrate(G: nx.Graph(), tau: float, x0: np.ndarray, t_end: int=1e7, solout_point = '') -> np.ndarray:
    """Integrate the generalized Lotka-Volterra equations"""
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
    
        # Define the correct parameters
        A = nx.to_numpy_array(G)
        r = np.ones(len(G))
        M = -tau * A - np.identity(len(G))
        
        # Define the generalized Lotka-Volterra equations and it's jacobian
        f = lambda t, x : np.diag(x) @ ( r +  M @ x )
        J = lambda t, x : np.identity(r) + np.diag(x) @ M + np.diag(M@x)

        # Set integration methods.   
        ode15s = ode(f, J)
        ode15s.set_integrator('dopri5')
        
        # Stop integration upon bifurcation
        if solout_point != '':
            def solout(t, x):
                if min(x) < 1e-7:
                    return -1
                else:
                    return 0
                
            ode15s.set_solout(solout)

        ode15s.set_initial_value(x0, 0)
        
        # Integrate system.
        y = ode15s.integrate(t_end)
        y = np.transpose(y)
    
        return y
    
def F(point: np.ndarray) -> float:
    """Calculate product of array elements"""
    return np.prod(point)

def dxdtau(A: np.ndarray, M_inv: np.ndarray) -> np.ndarray:
    """Calculate derivative of interior fixed point as function of tau"""

    return - (M_inv @ A @ M_inv) @ np.ones(len(A))

def dFdtau(A: np.ndarray, M_inv: np.ndarray) -> float:
    """Calculate derivative of functional as function of tau"""
    
    derivatives = np.array(dxdtau(A, M_inv))
    point = M_inv @ np.ones(len(M_inv))
    products = np.array( [ np.prod( [ point[j] for j in range(len(point)) if j != i ] ) for i in range(len(point)) ] )
        
    return np.sum( derivatives * products )
    
def newtonmethod( F: callable, tau_initial: float, tolerance: float, G: nx.Graph() ) -> float:
    """Find bifurcation tau"""

    # Determine adjacency matrix
    A = nx.to_numpy_array(G)
    tau_max = 1 / abs( min( np.linalg.eigvals(A) ) )
    dt = 1e200

    tau = tau_initial
    iteration = 0
    while dt > tolerance and tau < tau_max and iteration < 500:
        M = tau * A + np.identity(len(G))

        try:
            M_inv = np.linalg.inv(M)
            point = M_inv @ np.ones(len(G))

            if abs(dFdtau(A, M_inv)) < 1e-200:
                break
            tau1 = tau - F(point) / dFdtau(A, M_inv)
                        
        except:
            break
        
        dt = abs(tau1 - tau)
        tau = tau1
        iteration += 1
    
    return min(tau, tau_max), min(tau, tau_max) == tau_max

if __name__ == '__main__':
    """Get all the necessary data for the figure."""
    A0_pitchfork = np.load(os.path.join(sys.path[0], 'Data/A0_pitchfork.npy'))
    G_pitchfork = nx.from_numpy_array(A0_pitchfork)

    G_transcritical = nx.from_numpy_array(A0_pitchfork)
    G_transcritical.add_edges_from([(1,3)])
    A0_transcritical = nx.to_numpy_array(G_transcritical)

    # Set tau-domain of the plot.
    tau_min, tau_max, step_size = 0.01, 1.1, 0.005
    domain = np.arange(0, tau_max+step_size, step_size)

    # Set initial values.
    x0_transcritical = [ 1 for i in range(len(A0_transcritical)) ]
    x0_pitchfork = [ 1 for i in range(len(A0_pitchfork)) ]
    output_arr_transcritical = []
    output_arr_pitchfork = []

    # Determine bifurcation values numerically
    bifurcation_point_transcritical = newtonmethod( F, 1e-30, 1e-50, G_transcritical )[0]
    bifurcation_point_pitchfork = newtonmethod( F, 1e-30, 1e-50, G_pitchfork )[0]

    for count, tau in enumerate(domain):
        # Integrate the system
        output_transcritical = LV_integrate(G_transcritical, tau, x0_transcritical)
        output_arr_transcritical.append(output_transcritical)
        x0_transcritical = output_transcritical   
        x0_transcritical = [ item if item < 1e-5 or item > 1-1e-5 else item + random.uniform(0,1e-5) for item in x0_transcritical ]

        # Integrate the system
        output_pitchfork = LV_integrate(G_pitchfork, tau, x0_pitchfork)
        output_arr_pitchfork.append(output_pitchfork)
        x0_pitchfork = output_pitchfork   
        x0_pitchfork = [ item if item < 1e-5 or item > 1-1e-5 else item + random.uniform(0,1e-5) for item in x0_pitchfork ]

        # Print how far we are with the calculations.
        print( f'{np.round((count+1) / len(domain) * 100, 2)}%' )

    np.save(os.path.join(sys.path[0], 'data/domain'), domain)
    np.save(os.path.join(sys.path[0], 'data/output_arr_transcritical'), output_arr_transcritical)
    np.save(os.path.join(sys.path[0], 'data/output_arr_pitchfork'), output_arr_pitchfork)

    pos = nx.spring_layout(G_transcritical)

    with open(os.path.join(sys.path[0], 'data/pos_pitchfork.npy'), "wb") as f:
        pickle.dump(pos, f)
            
    with open(os.path.join(sys.path[0], 'data/pos_transcritical.npy'), "wb") as f:
        pickle.dump(pos, f)
        
    # Determine bifurcation values numerically
    bifurcation_point_transcritical = newtonmethod( F, 1e-30, 1e-50, G_transcritical )[0]
    bifurcation_point_pitchfork = newtonmethod( F, 1e-30, 1e-50, G_pitchfork )[0]
    
    np.save(os.path.join(sys.path[0], 'data/bifurcation_points'), [bifurcation_point_transcritical, bifurcation_point_pitchfork])