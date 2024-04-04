import numpy as np
import networkx as nx
import sys
import os
import pandas as pd
from typing import Optional

def binomial_graph(size: int, p: float, dmax: int, connected: bool = False) -> nx.Graph:
    """
    Generate a random graph with a binomial degree distribution.

    Parameters:
        size (int): The number of nodes in the graph.
        p (float): The probability of connecting each pair of nodes.
        dmax (int): The maximum degree of each node.
        connected (bool, optional): Whether the generated graph should be connected. Defaults to False.

    Returns:
        nx.Graph: A generated graph.
    """
    # Validate input parameters
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Size must be a positive integer.")
    if not 0 <= p <= 1:
        raise ValueError("Probability p must be in the range [0, 1].")
    if not isinstance(dmax, int) or dmax <= 0:
        raise ValueError("Maximum degree (dmax) must be a positive integer.")
    
    # Run until we have a connected graph if required
    while True:
        # Generate degree sequence
        while True:
            degree_sequence = np.random.binomial(dmax, p, size=size)
            is_graphical = nx.is_graphical(degree_sequence)
            
            if is_graphical:
                break
    
        # Generate a graph with the given degree sequence
        G = nx.configuration_model(degree_sequence)
        mapping = {node: node + 1 for node in G.nodes()}
        G = nx.relabel_nodes(G, mapping)
        G = nx.Graph(G)
        G.remove_edges_from(nx.selfloop_edges(G))
        
        # If not required to be connected, return the graph
        if not connected:
            return G
        
        # Check if the graph is connected
        if nx.is_connected(G):  
            return G
        
def generate_graphs():
    # Specify parameters
    size_min, size_max, sizestep = 50, 150, 10
    size_domain = np.arange(size_min, size_max+1, sizestep)

    p_min, p_max, p_sizestep = 0.2, 0.95, 0.05
    p_domain = np.arange(p_min, p_max+p_sizestep, p_sizestep)

    runs, dmax, data = 100, 30, []

    # Generate graphs
    index = 1
    for size in size_domain:
        for p_connection in p_domain:
            for i in range(runs):
                G = binomial_graph(int(size), p_connection, int(dmax), connected=True)
                degrees = [ G.degree(node) for node in G ]

                new_row = {
                    'type': 'binomial',
                    'size': len(G),
                    'p_connection': p_connection,
                    'vertices': G.nodes(), 
                    'edges': G.edges(), 
                    'dmax': max(degrees),
                    'analytical_value': None, 
                    'bound_value': None
                    }
                
                data.append(new_row)

                percentage = np.round((index) / (len(size_domain) * len(p_domain) * runs) * 100 , 2)
                print(f'{percentage} %', end='\r')
                
                index += 1

    df = pd.DataFrame(data)

    # Save raw data in the same directory as the file.
    df.to_csv(os.path.join(sys.path[0], f'data_empty/data_raw.csv'), index=False)
    df.to_pickle(os.path.join(sys.path[0], f'data_empty/data_raw.pkl'))
    
if __name__ == '__main__':
    generate_graphs()