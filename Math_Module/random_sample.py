import random

a= random.random()
print(a)

b=random.uniform(0,10)
print(b)

c=random.randint(1,100)
print(c)

d=random.randrange(1,10,2)
print(d)

random.seed(100)
e=random.random()
print(e)