import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pickle
import matplotlib.gridspec as gridspec

# import data
A0_transcritical = np.load(os.path.join(sys.path[0], 'data/A0_transcritical.npy'))
A0_pitchfork = np.load(os.path.join(sys.path[0], 'data/A0_pitchfork.npy'))
output_arr_transcritical = np.load(os.path.join(sys.path[0], 'data/output_arr_transcritical.npy'), allow_pickle=True)
output_arr_pitchfork = np.load(os.path.join(sys.path[0], 'data/output_arr_pitchfork.npy'), allow_pickle=True)
bifurcation_point_transcritical, bifurcation_point_pitchfork = np.load(os.path.join(sys.path[0], 'data/bifurcation_points.npy'))
domain = np.load(os.path.join(sys.path[0], 'data/domain.npy'))

with open(os.path.join(sys.path[0], 'data/pos_transcritical.npy'), 'rb') as file:
    pos = pickle.load(file)

# Define values
G_transcritical = nx.from_numpy_array(A0_transcritical)
G_pitchfork = nx.from_numpy_array(A0_pitchfork)

fig, (ax1, ax2) = plt.subplots(ncols=1, nrows=2, figsize=(10,8))
fig.subplots_adjust(wspace=0.3, hspace=0.45)

cud_palette = [
    '#4682B4',   # Steel blue
    '#E69F00',  # Orange
    '#000000',  # Black
    '#a5682a',  # Brown
    '#CC61B0',  # Pink
    '#8A2BE2',  # Blue violet
    '#0101fd',  # Blue
    '#ff0101'   # Red
]

# Plot data
size = 40
skip = 10
markers = ['o', 's', 'D', '^', 'v', 'p', 'H', '*']
labels ={0: r'$x^*_1$', 1: r'$x^*_2$', 2: r'$x^*_3$', 3: r'$x^*_4$', 4: r'$x^*_5$', 5: r'$x^*_6$', 6: r'$x^*_7$', 7: r'$x^*_8$'}

# -x1
ax1.plot(domain[domain < bifurcation_point_transcritical], 
         output_arr_transcritical[:,0][domain < bifurcation_point_transcritical], 
         color=cud_palette[0])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical][::skip],
            y = output_arr_transcritical[:,0][domain < bifurcation_point_transcritical][::skip],
            color=cud_palette[0], 
            s=size, 
            marker=markers[0], 
            label=labels[0], 
            facecolors='none', 
            edgecolors=cud_palette[0])

ax1.plot(domain[domain > bifurcation_point_transcritical-0.005], 
         output_arr_transcritical[:,0][domain > bifurcation_point_transcritical-0.005], 
         color=cud_palette[0])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical][::skip],
            y = output_arr_transcritical[:,0][domain > bifurcation_point_transcritical][::skip],
            color=cud_palette[0], 
            s=size, 
            marker=markers[0], 
            facecolors='none', 
            edgecolors=cud_palette[0])

# -x2
ax1.plot(domain[domain < bifurcation_point_transcritical+0.01], 
         output_arr_transcritical[:,1][domain < bifurcation_point_transcritical+0.01], 
         color=cud_palette[1])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical-0.001][::skip],
            y = output_arr_transcritical[:,1][domain < bifurcation_point_transcritical-0.001][::skip],
            color=cud_palette[1], 
            s=size, 
            marker=markers[1], 
            label=labels[1], 
            facecolors='none', 
            edgecolors=cud_palette[1])

ax1.plot(domain[domain > bifurcation_point_transcritical+0.001], 
         output_arr_transcritical[:,1][domain > bifurcation_point_transcritical+0.001], 
         color=cud_palette[1])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical+0.001][int(skip/2)::skip],
            y = output_arr_transcritical[:,1][domain > bifurcation_point_transcritical+0.001][int(skip/2)::skip],
            color=cud_palette[1], 
            s=size, 
            marker=markers[1], 
            facecolors='none', 
            edgecolors=cud_palette[1])

# -x3
ax1.plot(domain[domain < bifurcation_point_transcritical+0.005], 
         output_arr_transcritical[:,2][domain < bifurcation_point_transcritical+0.005], 
         color=cud_palette[2])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical+0.001][::skip],
            y = output_arr_transcritical[:,2][domain < bifurcation_point_transcritical+0.001][::skip],
            color=cud_palette[2],
            s=size, 
            marker=markers[2], 
            label=labels[2], 
            facecolors='none', 
            edgecolors=cud_palette[2])

ax1.plot(domain[domain > bifurcation_point_transcritical+0.001], 
         output_arr_transcritical[:,2][domain > bifurcation_point_transcritical+0.001], 
         color=cud_palette[2],
         dashes=[0, 15, 15, 0])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical+0.001][::skip],
            y = output_arr_transcritical[:,2][domain > bifurcation_point_transcritical+0.001][::skip],
            color=cud_palette[2],
            s=size, 
            marker=markers[2], 
            facecolors='none', 
            edgecolors=cud_palette[2])

# -x4
ax1.plot(domain[domain < bifurcation_point_transcritical+0.001], 
         output_arr_transcritical[:,3][domain < bifurcation_point_transcritical+0.001], 
         color=cud_palette[3])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical+0.001][::skip],
            y = output_arr_transcritical[:,3][domain < bifurcation_point_transcritical+0.001][::skip],
            color=cud_palette[3], 
            s=size, 
            marker=markers[3], 
            label=labels[3], 
            facecolors='none', 
            edgecolors=cud_palette[3])

ax1.plot(domain[domain > bifurcation_point_transcritical], 
         output_arr_transcritical[:,3][domain > bifurcation_point_transcritical], 
         color=cud_palette[3],
         dashes=[0, 15, 15, 0])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical][int(skip/2)::skip],
            y = output_arr_transcritical[:,3][domain > bifurcation_point_transcritical][int(skip/2)::skip],
            color=cud_palette[3], 
            s=size, 
            marker=markers[3], 
            facecolors='none', 
            edgecolors=cud_palette[3])
    
# -x5
ax1.plot(domain[domain < bifurcation_point_transcritical+0.001], 
         output_arr_transcritical[:,4][domain < bifurcation_point_transcritical+0.001], 
         color=cud_palette[4])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical][::skip],
            y = output_arr_transcritical[:,4][domain < bifurcation_point_transcritical][::skip],
            color=cud_palette[4], 
            s=size, 
            marker=markers[4], 
            label=labels[4], 
            facecolors='none', 
            edgecolors=cud_palette[4])

ax1.plot(domain[domain > bifurcation_point_transcritical-0.001], 
         output_arr_transcritical[:,4][domain > bifurcation_point_transcritical-0.001], 
         color=cud_palette[4])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical+0.001][::skip],
            y = output_arr_transcritical[:,4][domain > bifurcation_point_transcritical+0.001][::skip],
            color=cud_palette[4],
            s=size, 
            marker=markers[4], 
            facecolors='none', 
            edgecolors=cud_palette[4])

# -x6
ax1.plot(domain, output_arr_transcritical[:,5], color=cud_palette[5])
ax1.scatter(x=domain[::skip],
            y = output_arr_transcritical[:,5][::skip],
            color=cud_palette[5], 
            s=size, 
            marker=markers[5], 
            label=labels[5], 
            facecolors='none', 
            edgecolors=cud_palette[5])

# -x7
ax1.plot(domain[domain < bifurcation_point_transcritical+0.005], 
         output_arr_transcritical[:,6][domain < bifurcation_point_transcritical+0.005], 
         color=cud_palette[6])
ax1.scatter(x=domain[domain < bifurcation_point_transcritical][::skip],
            y = output_arr_transcritical[:,6][domain < bifurcation_point_transcritical][::skip],
            color=cud_palette[6], 
            s=size, 
            marker=markers[6], 
            label=labels[6], 
            facecolors='none', 
            edgecolors=cud_palette[6])

ax1.plot(domain[domain > bifurcation_point_transcritical+0.01], 
         output_arr_transcritical[:,6][domain > bifurcation_point_transcritical+0.01], 
         color=cud_palette[6],
         dashes=[0, 15, 15, 0])
ax1.scatter(x=domain[domain > bifurcation_point_transcritical][int(skip/2)::skip],
            y = output_arr_transcritical[:,6][domain > bifurcation_point_transcritical][int(skip/2)::skip],
            color=cud_palette[6], 
            s=size, 
            marker=markers[6], 
            facecolors='none', 
            edgecolors=cud_palette[6])

# -x8
ax1.plot(domain, output_arr_transcritical[:,7], color=cud_palette[7])
ax1.scatter(x=domain[::skip],
            y = output_arr_transcritical[:,7][::skip],
            color=cud_palette[7], 
            s=size, 
            marker=markers[7], 
            label=labels[7], 
            facecolors='none', 
            edgecolors=cud_palette[7])

# Draw network
# Manually define position and size for the inset plot
inset_x = 0.22
inset_y = 0.57
inset_width = 0.17
inset_height = 0.15
ax1_inset = fig.add_axes([inset_x, inset_y, inset_width, inset_height])

x_min, x_max, y_min, y_max = min([arr[0]for arr in list(pos.values())]), max([arr[0]for arr in list(pos.values())]), min([arr[1]for arr in list(pos.values())]), max([arr[1]for arr in list(pos.values())])
ax1_inset.set_xlim(-0.54, 0.65)
ax1_inset.set_ylim(-0.72, 0.97)

node_color_pitchfork = [ '#0101fd' for i in range(len(G_transcritical)) ]
node_color_pitchfork[7] = '#E69F00'

nx.draw_networkx(G_transcritical, ax=ax1_inset, pos=pos, with_labels=False, node_size=350, node_color=node_color_pitchfork, edge_color='k', width=3, edgecolors='black')
nx.draw_networkx_labels(G_transcritical, ax=ax1_inset, pos=pos, labels={i : str(i+1) for i in range(len(G_transcritical))}, font_size=11, font_color='white')

ax1.set_xlim(0, 0.55)
ax1.legend(loc='lower left', fontsize=10)
ax1.set_xlabel(r'$\tau$', fontsize=16)
ax1.set_ylabel(r'$x^*$', fontsize=16)
ax1.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], ['0', '0.1', '0.2', '0.3', '0.4', '0.5'], fontsize=14)
ax1.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=14)
ax1.axvline(bifurcation_point_transcritical, 0, 0.2, color='grey', linestyle=':', clip_on=False)
ax1.text(bifurcation_point_transcritical+0.002, 0.08, r'$\tau_{\text{trans}}$', fontsize=15)
ax1.set_title('(a)', fontsize=16)

# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------

# Plot data
size = 40
skip = 10
markers = ['o', 's', 'D', '^', 'v', 'p', 'H', '*']
labels ={0: r'$x^*_1$', 1: r'$x^*_2$', 2: r'$x^*_3$', 3: r'$x^*_4$', 4: r'$x^*_5$', 5: r'$x^*_6$', 6: r'$x^*_7$', 7: r'$x^*_8$'}

# -x1
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.001], 
         output_arr_pitchfork[:,0][domain < bifurcation_point_pitchfork-0.001], 
         color=cud_palette[0])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            y = output_arr_pitchfork[:,0][domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            color=cud_palette[0], 
            s=size, 
            marker=markers[0], 
            label=labels[0], 
            facecolors='none', 
            edgecolors=cud_palette[0])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,0][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[0])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][::skip],
            y = output_arr_pitchfork[:,0][domain > bifurcation_point_pitchfork+0.01][::skip],
            color=cud_palette[0], 
            s=size, 
            marker=markers[0], 
            facecolors='none', 
            edgecolors=cud_palette[0])

# -x2
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.001], 
         output_arr_pitchfork[:,1][domain < bifurcation_point_pitchfork-0.001], 
         color=cud_palette[1])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            y = output_arr_pitchfork[:,1][domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            color=cud_palette[1], 
            s=size, 
            marker=markers[1], 
            label=labels[1], 
            facecolors='none', 
            edgecolors=cud_palette[1])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,1][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[1])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][::skip],
            y = output_arr_pitchfork[:,1][domain > bifurcation_point_pitchfork+0.01][::skip],
            color=cud_palette[1], 
            s=size, 
            marker=markers[1], 
            facecolors='none', 
            edgecolors=cud_palette[1])

# -x3
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.001], 
         output_arr_pitchfork[:,2][domain < bifurcation_point_pitchfork-0.001], 
         color=cud_palette[2])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            y = output_arr_pitchfork[:,2][domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            color=cud_palette[2],
            s=size, 
            marker=markers[2], 
            label=labels[2], 
            facecolors='none', 
            edgecolors=cud_palette[2])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,2][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[2],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            y = output_arr_pitchfork[:,2][domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            color=cud_palette[2],
            s=size, 
            marker=markers[2], 
            facecolors='none', 
            edgecolors=cud_palette[2])

# -x4
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.001], 
         output_arr_pitchfork[:,3][domain < bifurcation_point_pitchfork-0.001], 
         color=cud_palette[3])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            y = output_arr_pitchfork[:,3][domain < bifurcation_point_pitchfork-0.001][int(skip/2)::skip],
            color=cud_palette[3], 
            s=size, 
            marker=markers[3], 
            label=labels[3], 
            facecolors='none', 
            edgecolors=cud_palette[3])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,3][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[3])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][::skip],
            y = output_arr_pitchfork[:,3][domain > bifurcation_point_pitchfork+0.01][::skip],
            color=cud_palette[3], 
            s=size, 
            marker=markers[3], 
            facecolors='none', 
            edgecolors=cud_palette[3])
    
# -x5
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.01], 
         output_arr_pitchfork[:,4][domain < bifurcation_point_pitchfork-0.01], 
         color=cud_palette[4],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][::skip],
            y = output_arr_pitchfork[:,4][domain < bifurcation_point_pitchfork-0.001][::skip],
            color=cud_palette[4], 
            s=size, 
            marker=markers[4], 
            label=labels[4], 
            facecolors='none', 
            edgecolors=cud_palette[4])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,4][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[4],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            y = output_arr_pitchfork[:,4][domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            color=cud_palette[4], 
            s=size, 
            marker=markers[4], 
            facecolors='none', 
            edgecolors=cud_palette[4])

# -x6
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.01], 
         output_arr_pitchfork[:,5][domain < bifurcation_point_pitchfork-0.01], 
         color=cud_palette[5],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][::skip],
            y = output_arr_pitchfork[:,5][domain < bifurcation_point_pitchfork-0.001][::skip],
            color=cud_palette[5], 
            s=size, 
            marker=markers[5], 
            label=labels[5], 
            facecolors='none', 
            edgecolors=cud_palette[5])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,5][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[5])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][::skip],
            y = output_arr_pitchfork[:,5][domain > bifurcation_point_pitchfork+0.01][::skip],
            color=cud_palette[5], 
            s=size, 
            marker=markers[5], 
            facecolors='none', 
            edgecolors=cud_palette[5])

# -x7
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.01], 
         output_arr_pitchfork[:,6][domain < bifurcation_point_pitchfork-0.01], 
         color=cud_palette[6],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][::skip],
            y = output_arr_pitchfork[:,6][domain < bifurcation_point_pitchfork-0.001][::skip],
            color=cud_palette[6], 
            s=size, 
            marker=markers[6], 
            label=labels[6], 
            facecolors='none', 
            edgecolors=cud_palette[6])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,6][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[6],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            y = output_arr_pitchfork[:,6][domain > bifurcation_point_pitchfork+0.01][int(skip/2)::skip],
            color=cud_palette[6], 
            s=size, 
            marker=markers[6], 
            facecolors='none', 
            edgecolors=cud_palette[6])

# -x8
ax2.plot(domain[domain < bifurcation_point_pitchfork-0.01], 
         output_arr_pitchfork[:,7][domain < bifurcation_point_pitchfork-0.01], 
         color=cud_palette[7],
         dashes=[0, 15, 15, 0])
ax2.scatter(x=domain[domain < bifurcation_point_pitchfork-0.001][::skip],
            y = output_arr_pitchfork[:,7][domain < bifurcation_point_pitchfork-0.001][::skip],
            color=cud_palette[7], 
            s=size, 
            marker=markers[7], 
            label=labels[7], 
            facecolors='none', 
            edgecolors=cud_palette[7])

ax2.plot(domain[domain > bifurcation_point_pitchfork+0.01], 
         output_arr_pitchfork[:,7][domain > bifurcation_point_pitchfork+0.01], 
         color=cud_palette[7])
ax2.scatter(x=domain[domain > bifurcation_point_pitchfork+0.01][::skip],
            y = output_arr_pitchfork[:,7][domain > bifurcation_point_pitchfork+0.01][::skip],
            color=cud_palette[7], 
            s=size, 
            marker=markers[7], 
            facecolors='none', 
            edgecolors=cud_palette[7])

# Draw network
inset_x = 0.22
inset_y = 0.13
inset_width = 0.17
inset_height = 0.15
ax2_inset = fig.add_axes([inset_x, inset_y, inset_width, inset_height])

ax2_inset.set_xlim(-0.54, 0.65)
ax2_inset.set_ylim(-0.72, 0.97)

node_color_pitchfork = [ '#0101fd' for i in range(len(G_transcritical)) ]
node_color_pitchfork[7] = '#E69F00'

nx.draw_networkx(G_pitchfork, ax=ax2_inset, pos=pos, with_labels=False, node_size=350, node_color=node_color_pitchfork, edge_color='k', width=3, edgecolors='black')
nx.draw_networkx_labels(G_pitchfork, ax=ax2_inset, pos=pos, labels={i : str(i+1) for i in range(len(G_pitchfork))}, font_size=11, font_color='white')

ax2.set_xlim(0, 0.55)
ax2.legend(loc='lower left', fontsize=10)
ax2.set_xlabel(r'$\tau$', fontsize=16)
ax2.set_ylabel(r'$x^*$', fontsize=16)
ax2.set_xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5], ['0', '0.1', '0.2', '0.3', '0.4', '0.5'], fontsize=14)
ax2.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=14)
ax2.axvline(bifurcation_point_pitchfork+0.007, 0, 0.2, color='grey', linestyle=':', clip_on=False)
ax2.text(bifurcation_point_pitchfork+0.009, 0.08, r'$\tau_{\text{pitch}}$', fontsize=15)
ax2.set_title('(a)', fontsize=16)

plt.savefig(os.path.join(sys.path[0], 'Figure2.pdf'), dpi=900, transparent=True, bbox_inches='tight')
plt.show()