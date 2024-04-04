import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys

cud_palette = [
    '#E69F00',  # Orange
    '#0101fd',  # Blue
    '#ff0101',   # Red
]

df = pd.read_pickle(os.path.join(sys.path[0], 'data_analysed/data_raw.pkl'))

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10,5))
fig.subplots_adjust(wspace=0.3)

# Make plot 1
for index, p in enumerate([0.2, 0.5, 0.8]):
    
    color = cud_palette[index]
    df_p = df[np.round(df['p_connection'],2) == p]

    ax1.plot(df_p['size'], df_p['ratio_mean'], marker='o', linestyle='-', color=color, label=f'p={np.round(p,2)}', markersize=5, linewidth=1.5)
    
    ax1.errorbar(df_p['size'], df_p['ratio_mean'], yerr=(df_p['ratio_mean'] - df_p['lower_bound'], df_p['upper_bound'] - df_p['ratio_mean']), color=color, capsize=5, capthick=1.5, elinewidth=1.5)
        
ax1.set_xlabel('Size (n)', fontsize=16)
ax1.set_ylabel(r'Mean ratio $\tau_{c} / \Omega$', fontsize=16)
ax1.legend()
ax1.set_title('(a)', fontsize=16)
ax1.set_xticks([50, 75, 100, 125, 150], [50, 75, 100, 125, 150], fontsize=14)
ax1.set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45], [0.2, 0.25, 0.3, 0.35, 0.4, 0.45], fontsize=14)
ax1.grid()

# Make plot 2
color = cud_palette[index]
df_size = df[df['size'] == 100]
ax2.plot(df_size['p_connection'], df_size['ratio_mean'], marker='o', linestyle='-', color='#000000', label=f'p={np.round(p,2)}', markersize=5, linewidth=1.5)
ax2.errorbar(df_size['p_connection'], df_size['ratio_mean'], yerr=(df_size['ratio_mean'] - df_size['lower_bound'], df_size['upper_bound'] - df_size['ratio_mean']), color='#000000', fmt='o', capsize=5, capthick=1.5, elinewidth=1.5)

ax2.set_xlabel(r'$p$', fontsize=16)
ax2.set_ylabel(r'Mean ratio $\tau_{c} / \Omega$', fontsize=16)
ax2.set_title('(b)', fontsize=16)
ax2.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], [0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14)
ax2.set_yticks([0.2, 0.25, 0.3, 0.35, 0.4, 0.45], [0.2, 0.25, 0.3, 0.35, 0.4, 0.45], fontsize=14)
ax2.set_xlim(0.15, 1)
ax2.grid()

plt.savefig(os.path.join(sys.path[0], 'Figure3.pdf'), dpi=600, transparent=True, bbox_inches='tight')
plt.show()    