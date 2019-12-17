"""Plots the generated points to a graph for each value of w"""
import os

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot():
    # Saves 21 colours from the rainbow colormap to use for each value of x
    colours = mpl.cm.rainbow(np.linspace(0, 1, 21))

    # Makes a plot for each value of w
    for i in range(20 + 1):
        print('Plotting Plot {}'.format(i))
        folder_name = 'csv{:0>2d}'.format(i)
        fig = plt.figure()
        ax1 = fig.add_subplot(1, 1, 1, projection='3d')
        for j in range(20 + 1):
            points = np.genfromtxt(os.path.join(folder_name, \
                'file{:0>2d}.csv'.format(j)), delimiter=',')
            y = points[:, 2]
            z = points[:, 3]
            f = points[:, 4]
            ax1.plot_trisurf(y, z, f, color=colours[j])
        ax1.set_xlabel('y', fontsize=15)
        ax1.set_ylabel('z', fontsize=15)
        ax1.set_zlabel('f', fontsize=15)
        fig.suptitle('w = {}'.format(i - 10), fontsize=20)
        ax1.view_init(elev=30, azim=-15)

    # Creates the colorbar legend at the bottom
        ax2 = plt.axes([0.03, 0.05, 0.94, 0.02])
        cmap = mpl.cm.rainbow
        norm = mpl.colors.Normalize(vmin=-10, vmax=10)
        cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm, \
            orientation='horizontal')
        cb.set_label('x', fontsize=15)

        fig.set_size_inches(16, 10)
        # plt.show()
        plt.savefig(os.path.join(folder_name, 'plot{:0>2d}.png'.format(i)))
        plt.close()

if __name__ == "__main__":
    plot()
