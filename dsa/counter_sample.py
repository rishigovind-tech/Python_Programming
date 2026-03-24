 
from collections import Counter
 
L = ['Mark', 'Jonny', 'David', 'Mark', 'Jonny', 'Mark', 'James', 'Mathew']

c=Counter(L)
print(c)

print(c.keys())

c.elements()

for i in c.elements():
    print(i)
    
c.pop('Ajay')


# Counter methods 

# clear(): Removes all elements from the dictionary.
# copy(): Returns a shallow copy of the dictionary.
# get(key): Returns the value for the specified key if the key is in the dictionary.
# items(): Returns a view object containing tuples of the dictionary's (key, value) pairs.
# keys(): Returns a view object containing the dictionary's keys.
# values(): Returns a view object containing the dictionary's values.
# update(): Updates the dictionary with elements from another dictionary or iterable.
# most_common(): Usually a method of collections.Counter, returning a list of the most frequent elements.
# pop(key): Removes and returns the value for the specified key.
# popitem(): Removes and returns the last inserted (key, value) pair.