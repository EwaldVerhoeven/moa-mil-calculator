import numpy as np
import matplotlib.pyplot as plt

# generate some random points
n = 200
x = 4 * np.random.randn(n) + 15
y = 2 * np.random.randn(n) + 10

print(type(x))

# somehow compute center of cloud, use e.g. medium or mean
x0 = np.median(x)
y0 = np.median(y)

# compute radius
r = np.sqrt((x - x0)**2 + (y - y0)**2)
t = 80 # percent
r0 = np.percentile(r, t)
n_within = (r < r0).sum()

# make plot    
plt.plot(x, y, '.')
circle = plt.Circle((x0, y0), r0, color='r', fill=False)
plt.gca().add_artist(circle)
plt.title('Found center at ({:.2f}, {:.2f})\n'
          '{}% radius is {:.2f}\n'
          '{} / {} points within circle'.format(
          x0, y0, t, r0, n_within, n))
plt.axis([0, 30, 0, 20])
plt.show()