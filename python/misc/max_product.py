import time,math
myList = [0,1,2,3,4,5,6,7]


# Given a list of integers it returns a list of list - all permutations
# ex: [2,3,1] => [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
def getAllListVariants(inList):
  list_len = len(inList)
  if list_len==1:
    return [inList]
  allVariants = []
  for i in range(list_len):
    elem = inList[i]
    listExcludingThisElem = inList[:i] + inList[i+1:]
    for myList in getAllListVariants(listExcludingThisElem):
      myList.append(elem)
      allVariants.append(myList)
  return allVariants

def progressBar(pct,i,totalCount):
  #global prev_pct
  new_pct = i*100/totalCount
  if new_pct>pct:
    #print pct,prev_pct
    if new_pct%10 == 0:
      print new_pct,
    else:
      print ".",
    pct=new_pct
  return pct

# Similar, but using iterator instead, it uses much less memory as long lists are not stored
# But runtime is about the same ~200 sec
def createIterator(inList):
  list_len = len(inList)
  if list_len==1:
    yield inList
  for i in range(list_len):
    elem = inList[i]
    for myList in createIterator(inList[:i] + inList[i+1:]):
      yield myList + [elem]

iterator = createIterator(myList)


start_time = time.time()    
num_len = len(myList)/2
cnt=0
maxProduct = 0

#for oneList in getAllListVariants(myList):
pct = 0
totalNumOfCombinations = math.factorial(len(myList))
for oneList in iterator:
  pct = progressBar(pct,cnt,totalNumOfCombinations)
  cnt +=1
  firstNumber = int(''.join(map(str,oneList[:num_len])))
  secondNumber = int(''.join(map(str,oneList[num_len:])))
  product = firstNumber * secondNumber
  if product > maxProduct:
    maxProduct = product
    maxFirst = firstNumber
    maxSecond = secondNumber 

run_time = int(time.time() - start_time)

print "\n\nTried",cnt,"variants in",run_time,"seconds"
print maxSecond
print "x"
print maxFirst
print "----------"
print maxProduct
#print getAllListVariants(myList)
