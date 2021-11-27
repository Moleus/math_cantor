
# cantor set from 0.5 to 0
# def divide(interval, level=1):
#     s = np.linspace(interval[0], interval[1], 4)
#     y = 0.5 ** level
#     plt.plot(s[1:3], [y, y], lw=2, solid_capstyle="butt")
#     if level < depth:
#         divide(s[:2], level+1)
#         divide(s[2:], level+1)

#%% cantor function(ladder)
from matplotlib import pyplot as plt
import numpy as np
import time

depth = 10
def divide(x_interval, y_interval, level=1):
    s = np.linspace(x_interval[0], x_interval[1], 4)
    y = np.sum(y_interval) / 2
    plt.plot(s[1:3], [y, y], lw=2, solid_capstyle="butt")
    if level < depth:
        divide(s[:2], [y_interval[0], y], level+1)
        divide(s[2:], [y, y_interval[1]], level+1)


st = time.perf_counter()
divide([0, 1], [0,1]) 
print(f"Total time for {depth} iterations: {st - time.perf_counter()}")
plt.gca()
plt.show()

exit(0)

#%%  cantor set
import numpy as np
import matplotlib.pyplot as plt

line = [0,1]
depth = 5

def divide(line, level=0):
    plt.plot(line,[level,level], color="k", lw=5, solid_capstyle="butt")
    if level < depth:
        s = np.linspace(line[0],line[1],4)
        divide(s[:2], level+1)
        divide(s[2:], level+1)

divide(line)
plt.gca().invert_yaxis()
plt.show()
