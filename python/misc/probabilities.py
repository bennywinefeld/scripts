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
for N in range(1, 100, 5):
    numOfTosses.append(N)
    orelRatio.append(float(tossCoin(N))/N)
    #print N," tosses", orelRatio, " orlov"
          
plt.plot([0,N],[0.5,0.5],'r',numOfTosses,orelRatio,'b')
plt.ylabel('Orel ratio')
plt.show()

