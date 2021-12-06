##%%  cantor set
#import numpy as np
#import matplotlib.pyplot as plt

#line = [0,1]
#depth = 5

#def divide(line, level=0):
#    plt.plot(line,[level,level], color="k", lw=5, solid_capstyle="butt")
#    if level < depth:
#        s = np.linspace(line[0],line[1],4)
#        divide(s[:2], level+1)
#        divide(s[2:], level+1)

#divide(line)
#plt.gca().invert_yaxis()
#plt.show()

#%% cantor set
from matplotlib import pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time


class CantorSet:
    def __init__(self, depth):
        self.points = [[], []]
        self.depth = depth
        self.fig, self.ax = self._prepear_plot()

    def divide(self, line, level=0):
        # self.points[0] += list(line)
        # self.points[1] += [level*0.1, level*0.1]
        plt.plot(line,[level,level], color="k", lw=5, solid_capstyle="butt")
        if level < self.depth:
            points = np.linspace(line[0], line[1], 4)
            self.divide(points[:2], level+1)
            self.divide(points[2:], level+1)

    def _prepear_plot(self,):
        fig = plt.figure(facecolor='w',figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.set_xlim([0, 1])
        # ax.set_ylim([0,1])
        return fig, ax
        
    def calculate_func(self):
        st = time.perf_counter()
        self.divide([0, 1]) 
        print(f"Total time for {depth} iterations: {time.perf_counter() - st}")

    def save_data(self):
        points = np.asarray(self.points)
        np.save(f"points_data_set_{self.depth}.npy", points)
        
    def load_data(self):   
        self.points = np.load(f"points_data_set_{self.depth}.npy").tolist()
        
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
        fn = 'animate_cantor_set'
        ani.save(fn+'.mp4',writer='ffmpeg',fps=20)


if __name__ == "__main__":
    depth = 10
    anim_frames = 150
    func = CantorSet(depth)

    func.calculate_func()
    # func.save_data()
    print("Data has been saved")
    plt.gca().invert_yaxis()
    plt.show()
    

    # func.load_data()
    # st = time.perf_counter()
    # func.plot_from_points()
    # print(f"plot_from_points {depth=}: {time.perf_counter() - st}")
    # plt.show()

    # func.create_animation(anim_frames)
    # print(f"create_animation {depth=}: {time.perf_counter() - st}")
