#from functools import reduce

# Find maximal product choosing a subset of list elements
def answer(xs):
    # Order of positive numbers doesn't matter
    Positives = [x for x in xs if x > 0]
    # Sort negatve numbers in descending order
    Negatives = sorted([x for x in xs if x < 0],reverse=True)
    # Special case - no positives and just one negative
    # if input list contained 0 - chose it, otherwise
    # pick the only negative number
    if((len(Positives) == 0) and (len(Negatives) == 1)):        
        if 0 in xs:
            return 0
        else:
            return Negatives[0]

    # If number of negative numbers is odd, drop the one
    # with smallest absolute value
    if (len(Negatives) % 2 == 1):
        CombinedList = Negatives[1:] + Positives
    else:
        CombinedList = Negatives + Positives

    # Multiply all elements in the combined list
    result = 1
    for elem in CombinedList:
        result *= elem
    
    return str(result)
    
    # If we had reduce function
    #return str(reduce((lambda x, y: x * y), Negatives + Positives))
  
xs = [-2,-7, -4]
print(answer(xs))
