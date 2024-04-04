import pandas as pd
import numpy as np
import os
import sys
from typing import List, Dict, Any, Union

def confidence_interval(data, confidence=0.95):

    data = np.array(data)    
    mean = np.mean(data)
    data_sorted = sorted(data)
    n = len(data)
        
    lower_index = int((n*(1-confidence)/2))
    upper_index = int(n - lower_index)
    
    data_filtered = data_sorted[lower_index:upper_index]

    lower_bound = data_filtered[0]
    upper_bound = data_filtered[-1]
    
    if lower_bound > mean:
        lower_bound = mean
    if upper_bound < mean:
        upper_bound = mean
    
    return lower_bound, upper_bound

def analyse_data(df: pd.DataFrame) -> None:
    """
    Analyze the data in the DataFrame and save the results as CSV and Pickle files.

    Parameters:
        df (pd.DataFrame): Input DataFrame containing the data to be analyzed.

    Returns:
        None
    """

    # List to store analyzed data
    data_analysed: List[Dict[str, Any]] = []

    # Iterate over unique 'p_connection' values
    for p in sorted(set(df['p_connection'])):
        df_p = df[df['p_connection'] == p]

        # Iterate over unique 'size' values within each 'p_connection'
        for size in sorted(set(df_p['size'])):
            df_p_size = df_p[df_p['size'] == size]

            # y = df_p_size['analytical_value'] / df_p_size['bound_value']
            y =  df_p_size['bound_value'] / df_p_size['analytical_value']
            
            lower_bound, upper_bound = confidence_interval(y, confidence=0.5)

            new_row = {
                'p_connection': p,
                'size': size,
                'ratio_mean': np.mean(y),
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }

            data_analysed.append(new_row)

    # Create DataFrame from analyzed data
    df_analysed = pd.DataFrame(data_analysed)

    # Save the analyzed data as CSV and Pickle files
    csv_path = os.path.join(sys.path[0], 'data_analysed/data_raw.csv')
    pickle_path = os.path.join(sys.path[0], 'data_analysed/data_raw.pkl')
    df_analysed.to_csv(csv_path, header=True, index=False)
    df_analysed.to_pickle(pickle_path)

if __name__ == '__main__':
    df = pd.read_pickle(os.path.join(sys.path[0], 'data_raw/data_raw.pkl'))
    analyse_data(df)