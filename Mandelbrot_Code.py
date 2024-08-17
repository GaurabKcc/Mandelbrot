import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def mandelbrot_iter(c, max_iter):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
    return max_iter

def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height, width))
    
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            mset[i, j] = mandelbrot_iter(c, max_iter)
            
    return mset

xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 1000, 1000
max_iter = 1000

mandelbrot_image = mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)


colors = [(0.5, 0.5, 1), (0, 0, 1), (0, 0, 0.5), (0,0,0)] 
n_bins = 100
custom_cmap = mcolors.LinearSegmentedColormap.from_list('black_to_blue', colors, N=n_bins)


plt.imshow(mandelbrot_image, extent=[xmin, xmax, ymin, ymax], cmap=custom_cmap, vmin=0, vmax=max_iter)
plt.colorbar()
plt.title('Mandelbrot Visualization')
plt.show()
