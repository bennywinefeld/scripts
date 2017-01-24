import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'r-', t, t**2, 'bs', t, t**3, 'g^')

# Set color of all graphs to green
#plt.setp(lines, color='g', linewidth=2.0)

plt.show()