from functools import reduce
values = [(2, 17), (1, 16), (3, 15), (4, 19)]
print("Original list")
print(values)

print("\nSort list by the first tuple element")
print(sorted(values))

print("\nSort list by the second tuple element, using returnSecondElement as a key")
def returnSecondElement(myTuple):
    return myTuple[1]
print (sorted(values, key=returnSecondElement))

print("\nSame, but using lambda, which is basically an anonymous function" )
print(sorted(values, key=lambda myTuple: myTuple[1]))

print("\nList comprehension. Construct a new list where each element is a sum of a tuple from original unsorted list") 
newList = [myTuple[0] + myTuple[1] for myTuple in values]
print(newList)

print("\nFinally extract elements which are >=17 and <=18\nCatch: filter() returns an iterable, not a list. Need list() fnction to convert to a list")
print(list(filter(lambda x : x >= 17 and x <= 18, range(20))))

# Use map function to create a list of squares
items = [1,2,3,4]
print(list(map((lambda x: x**2), items)))

# Could use the list comprehension to achieve the same thing
print([i**2 for i in items])

# Add alements of the list using reduce
list_of_numbers = [1, 5, 10, 100]
print(reduce(lambda x, y: x + y, list_of_numbers))