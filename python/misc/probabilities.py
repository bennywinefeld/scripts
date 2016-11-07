# Few examples of random numbers and probabilities

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Toss coin N times, return how many times we got '1'
def tossCoin(N):
    numOfOnes = 0
    random.seed()
    for num in range(1,N):
       if (random.randint(0,1) == 1):
            numOfOnes += 1
    return numOfOnes


numOfTosses = []
orelRatio = []
for N in range(1,10000,5):
    numOfTosses.append(N)
    orelRatio.append(float(tossCoin(N))/N)
    #print N," tosses", orelRatio, " orlov"
          
plt.plot([0,N],[0.5,0.5],'r',numOfTosses,orelRatio,'b')
plt.ylabel('Orel ratio')
plt.show()




# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
lines = plt.plot(t, t, 'r-', t, t**2, 'bs', t, t**3, 'g^')
# Set color of all graphs to green
plt.setp(lines, color='g', linewidth=2.0)

random.randint(a, b)

plt.show()