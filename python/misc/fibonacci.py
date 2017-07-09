# Calculate fibonacci value out of a given index
# for ex the sequence is 1, 1, 2, 3, 5, 8 ... than fib(6) =8 
import winsound
def fib(n):
    x,y = 0,1
    for i in range(2,n+1):
        x,y = y, x+y
    return y

x = 6
print('fib({:d})={:d}'.format(x,fib(x)))


def sumOfList(myList):
    total = 0
    for x in myList:
        total += x
    return(total)

# Need to find a sum of all list elements and multiply it by 2
winsound.Beep(440, 250) # frequency, duration



'''import winsound         # for sound  
import time             # for sleep

winsound.Beep(440, 250) # frequency, duration
time.sleep(0.25)        # in seconds (0.25 is 250ms)

winsound.Beep(600, 250)
time.sleep(0.25)'''
