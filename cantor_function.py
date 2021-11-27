#%% cantor function(ladder)

import matplotlib
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time


class CantorFunction:
    def __init__(self, depth):
        self.points = [[], []]
        self.depth = depth
        self.fig, self.ax = self._prepear_plot()

    def divide(self, x_interval, y_interval, level=1):
        s = np.linspace(x_interval[0], x_interval[1], 4)
        y = np.sum(y_interval) / 2
        self.points[0] += list(s[1:3])
        self.points[1] += [y,y]
        # plt.plot(s[1:3],[y,y], lw=3, marker=',')
        if level < self.depth:
            self.divide(s[:2], [y_interval[0], y], level+1)
            self.divide(s[2:], [y, y_interval[1]], level+1)

    def _prepear_plot(self,):
        fig = plt.figure(facecolor='w',figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.set_xlim([0, 1])
        ax.set_ylim([0,1])
        return fig, ax
        
    def calculate_func(self):
        st = time.perf_counter()
        self.divide([0, 1], [0,1]) 
        print(f"Total time for {depth} iterations: {time.perf_counter() - st}")

    def save_data(self):
        points = np.asarray(self.points)
        np.save(f"points_data_{self.depth}.npy", points)
        
    def load_data(self):   
        self.points = np.load(f"points_data_{self.depth}.npy").tolist()
        
    def plot_from_points(self):
        data = self.points[0]
        y_points = self.points[1]
        print(len(y_points))
        plt.hlines(y=y_points[::2], xmin=data[::2], xmax=data[1::2], lw=3, color='k', linestyle='-')

    def _animate(self, i, frames):
        y_en = 1 - i/(frames)
        x_en = y_en * (1 - i/frames)
            
        self.ax.set_xlim(0,x_en)
        self.ax.set_ylim(0,y_en)
        return self.fig,

    def create_animation(self, frames):
        ani = animation.FuncAnimation(self.fig, self._animate, fargs=(frames,),
                                       frames=frames, interval=10, blit=True)
        fn = 'animate_cantor'
        ani.save(fn+'.mp4',writer='ffmpeg',fps=20)


if __name__ == "__main__":
    depth = 18
    anim_frames = 150
    func = CantorFunction(depth)

    func.calculate_func()
    func.save_data()
    print("Data has been saved")

    # func.load_data()
    st = time.perf_counter()
    # func.plot_from_points()
    # print(f"plot_from_points {depth=}: {time.perf_counter() - st}")

    func.create_animation(anim_frames)
    print(f"create_animation {depth=}: {time.perf_counter() - st}")