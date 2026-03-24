import array

ar1=array.array('i',[10,20,30,40])
print(ar1)

s1=b'abcdef'
ar2=array.array('b',s1)
print(ar2)

print(ar1[1])

ar2.append(103)
print(ar2)

print(ar2.count(100))

ar2.extend([10,20,30,40])
print(ar2)

