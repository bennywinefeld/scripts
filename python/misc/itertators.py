def createIterator(inList):
  list_len = len(inList)
  if list_len==1:
    yield inList
  for i in range(list_len):
    elem = inList[i]
    #print(elem)
    for myList in createIterator(inList[:i] + inList[i+1:]):
      yield [elem] + myList
      

iterator = createIterator(["a","b","c"])
for elem in iterator:
    print(elem)