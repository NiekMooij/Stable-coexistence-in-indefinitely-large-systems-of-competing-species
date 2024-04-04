import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pickle
import matplotlib.gridspec as gridspec

with open(os.path.join(sys.path[0], 'data/pos_transcritical.npy'), 'rb') as file:
    pos = pickle.load(file)
    
pos[0] = [0.22, 0.75]
pos[1] = [-0.35, 0.6]
pos[2] = [0, 0.3 ]
pos[3] = [-0.42, -0.25]
pos[4] = [-0.17, -0.4]
pos[5] = [ 0.5, -0.5]
pos[6] = [0.5, 0.6]
pos[7] = [ 0.22 , -0.3]

with open(os.path.join(sys.path[0], 'data/pos_transcritical.npy'), "wb") as f:
    pickle.dump(pos, f)
    
with open(os.path.join(sys.path[0], 'data/pos_pitchfork.npy'), "wb") as f:
    pickle.dump(pos, f)
    
print(pos)