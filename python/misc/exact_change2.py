# List describing the total store of available coins
# [(25,4), (5,6)] means 4 quarters and 6 nickels
coinStore = [(25,4), (10,5),(5,5)]

# Given list of lists list1 = [[a1,b1,c1], [a2,b2,c2]] and list2 = [x, y]
# return [[a1,b1,c1,x], [a1,b1,c1,y], [a2,b2,c2,x] , [a2,b2,c2,y]] 
# The length of the new list becomes a multiple of lengths of two input lists
def createListCombos(list1,list2):
    result = []
    for subList in list1:
        for newElem in list2:
            result.append(subList+[newElem])
    return result

# Print how many coints of each denomination we have
print("Coin set:")
for (coinValue,coinCount) in coinStore:
    print("{}c - {} coins".format(coinValue,coinCount))
 
coinValue,coinAmount = coinStore[0]
coinSequences = [[(coinValue,count)] for count in range(coinAmount,-1,-1)]

# Create a list of possible coinSequences
# Ex for coinStore = [(25,2), (10,2)]
# coinSequences will be = [[(25, 2), (10, 2)], [(25, 2), (10, 1)], [(25, 2), (10, 0)], [(25, 1), (10, 2)], [(25, 1), (10, 1)], [(25, 1), (10, 0)], [(25, 0), (10, 2)], [(25, 0), (10, 1)], [(25, 0), (10, 0)]]
for coinValue,coinAmount in coinStore[1:]:
    coinVariants = [(coinValue,count) for count in range(coinAmount,-1,-1)]
    coinSequences = createListCombos(coinSequences,coinVariants)
print("{} possible coin sequences".format(len(coinSequences)))    

goodSequences = []
for sequence in coinSequences:
    sum = 0
    for (coinValue,coinCount) in sequence:
        sum += coinValue*coinCount
        if(sum>100):
            break

    if (sum==100):    
        goodSequences.append(sequence)
        
print("\n{} good coin sequences:".format(len(goodSequences)))    
for sequence in goodSequences:
    sequenceToDisplay = []
    for (coinValue,coinCount) in sequence:
        sequenceToDisplay += [coinValue for count in range(coinCount)]
    print(sequenceToDisplay)

