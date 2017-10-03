# Calculate fibonacci value out of a given index
# for ex the sequence is 1, 1, 2, 3, 5, 8 ... than fib(6) =8 
import winsound
def fib(n):
    x,y = 0,1
    for i in range(2,n+1):
        x,y = y, x+y
    return y

x = 3
print('fib({:d})={:d}'.format(x,fib(x)))

# Generate fibonaccy sequence with yield generator
def seqGen(x=0,y=1,len=5):
    for i in range(len): 
        x,y = y, x+y
        yield y

print([z for z in seqGen()])

def myFunc(n):
    if n==1:
        return 1
    else:
        return n*myFunc(n-1)

print(myFunc(4))

def sumOfList(myList):
    total = 0
    for x in myList:
        total += x
    return(total)



# Need to find a sum of all list elements and multiply it by 2
#winsound.Beep(440, 250) # frequency, duration



'''import winsound         # for sound  
import time             # for sleep

winsound.Beep(440, 250) # frequency, duration
time.sleep(0.25)        # in seconds (0.25 is 250ms)

winsound.Beep(600, 250)
time.sleep(0.25)'''
