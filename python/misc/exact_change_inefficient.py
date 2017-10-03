import time,math
myCoins = sorted([25,25,5])


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


subsetsWithSumOf100 = {}
for coinSet in  getAllListVariants(myCoins):
    print(coinSet)
    continue
    sum = 0
    coinSubset = []
    for coin in coinSet:
        sum += coin
        coinSubset.append(coin)
        if(sum==100):
            key = " ".join([str(coin) for coin in sorted(coinSubset,key=int, reverse=True)])
            if key not in subsetsWithSumOf100: 
                print(key)
                subsetsWithSumOf100[key] = 1
            break
        elif(sum>100):
            break