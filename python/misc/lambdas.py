values = [(2, 17), (1, 16), (3, 15), (4, 19)]
print "Original list"
print values

print "\nSort list by the first tuple element"
print sorted(values)

print "\nSort list by the second tuple element, using returnSecondElement as a key"
def returnSecondElement(myTuple):
    return myTuple[1]
print sorted(values, key=returnSecondElement)

print "\nSame, but using lambda, which is basically an anonymous function" 
print sorted(values, key=lambda myTuple: myTuple[1])

print "\nList comprehension. Construct a new list where each element is a sum of a tuple from original unsorted list" 
newList = [myTuple[0] + myTuple[1] for myTuple in values]
print newList

print "\nFinally extract elements which are >=17 and <=18"
print filter(lambda x : x >= 17 and x <= 18, newList)
