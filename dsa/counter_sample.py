 
from collections import Counter
 
L = ['Mark', 'Jonny', 'David', 'Mark', 'Jonny', 'Mark', 'James', 'Mathew']

c=Counter(L)
print(c)

print(c.keys())

c.elements()

for i in c.elements():
    print(i)