# List describing the total store of available coins
# [(25,4), (5,6)] means 4 quarters and 6 nickels
coinStore = [(25,6), (10,5),(5,5)]
print("Coin set:")
for (coinValue,coinCount) in coinStore:
    print("{}c - {} coins".format(coinValue,coinCount))
 
# Iterator which creates all possible combinations of elements in the  provided list
def createIterator(inList):
  list_len = len(inList)
  if list_len==1:
    yield inList
  for i in range(list_len):
    elem = inList[i]
    for myList in createIterator(inList[:i] + inList[i+1:]):
      yield myList + [elem]

# Now create all possible combinations of coin pairs
# ex: [(25,3), (10,2)] , [(10,2),(25,3)]
iterator = createIterator(coinStore)

allExpandedSequences = []
for compressedSequence in iterator:
    # compressedSequence ex: [(25,3) , (10,2)]
    # expandedSequences will be: [25, 25, 25, 10, 10], [25, 25, 25, 10], [25, 25, 10, 10], [25, 25, 10], [25, 10, 10], [25, 10]
    expandedSequences = []
    
    #print("compressedSequence = {} ".format(compressedSequence))
    for (coinValue, coinAmount) in compressedSequence:
        # (25,3) => [[25], [25, 25], [25, 25, 25]]
        coinVariants = [[coinValue]*amount for amount in range(1,coinAmount+1)]
        #print(coinVariants)
        if len(expandedSequences) == 0:
            expandedSequences = coinVariants
        else:
            newExpandedSequences = []
            for sequence in expandedSequences:
                for variant in coinVariants:                   
                    newExpandedSequences.append(sequence + variant)
            expandedSequences = newExpandedSequences
    allExpandedSequences += expandedSequences
    #print(expandedSequences)

allExpandedSequences = sorted(allExpandedSequences,reverse=True)
#print("All expanded sequences: {}".format(allExpandedSequences))

goodSequences = []
for sequence in allExpandedSequences:
    sum = 0
    for i in range(len(sequence)):
        sum += sequence[i]
        if(sum==100):
            goodSequences.append(tuple(sorted(sequence[:i+1],reverse=True)))

goodSequences = sorted(set(goodSequences),reverse=True)
print("\nFound {} variants".format(len(goodSequences)))
for sequence in goodSequences:
    print(sequence)
            

