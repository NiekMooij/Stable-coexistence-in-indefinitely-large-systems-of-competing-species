import numpy as np
import networkx as nx
import sys
import os
import time
import pandas as pd
import datetime

from get_first_bifurcation import get_first_bifurcation

def update_row(row: dict) -> dict:
    """Calculate output values and update row."""
    
    if row['analytical_value'] is None or row['bound_value'] is None:
                
        # Define networkx graph
        G = nx.Graph()
        G.add_nodes_from(row['vertices'])
        G.add_edges_from(row['edges'])

        degrees = [ G.degree(node) for node in G ]
        alpha = min(degrees) / max(degrees)
        theta = ( 2 + 9 * alpha**2 - 27 * alpha**4 ) / ( 2 * ( 1 + 3 * alpha**2 )**(3/2) )
        bound_value = 1 / max(degrees) * ( 1 / (3 * alpha**2) - ( 2 * np.sqrt(1 + 3 * alpha**2) ) / ( 3 * alpha**2 ) * np.sin( 1 / 3 * np.arcsin(theta) ) )
        
        analytical_value = get_first_bifurcation(G, tau_initial=1e-20, tolerance=1e-8)[0]

        if analytical_value < bound_value:
            print(f'Analytical value {analytical_value} is below the bound value {bound_value}.')
            exit()
        
        row['analytical_value'] = analytical_value
        row['bound_value'] = bound_value

        return row, True
    
    return row, False

def save_data(df: pd.DataFrame, type: str):
    """Save dataframe to csv and pickle format."""
    start_time = time.time()
    df.to_csv(os.path.join(sys.path[0], 'data_raw/data_raw.csv'), header=True, index=False)
    df.to_pickle(os.path.join(sys.path[0], 'data_raw/data_raw.pkl'))
    save_time = time.time() - start_time  
    print(f'Data saved in {np.round(save_time,3)} seconds.')
    
def analyse_graphs(save_after_n_runs=100):
    
    if os.path.exists(os.path.join(sys.path[0], 'data_empty/data_raw.pkl')):
        df = pd.read_pickle(os.path.join(sys.path[0], 'data_empty/data_raw.pkl'))
    else:
        print('No test graphs generated.')

    count = 0
    
    for index, row in df.iterrows():
        row_updated, update_flag = update_row(row)
        df.iloc[index] = pd.Series(row_updated)
        
        if update_flag:
            count += 1

        if (count+1) % save_after_n_runs == 0 or index+1 == len(df):
            save_data(df, type)
            
        print(f'Network analysed - {datetime.datetime.now()}')
                
if __name__ == '__main__':
    analyse_graphs(save_after_n_runs=10000)
