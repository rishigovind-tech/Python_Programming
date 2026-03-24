import bisect

L=[10,20,30,40,50,60,70,80,90]

bisect.insort(L,25)
print(L)

bisect.insort_left(L,100)
print(L)

bisect.insort_right(L,500)
print(L)

print(id(L[9]))
print(id(L[10]))
