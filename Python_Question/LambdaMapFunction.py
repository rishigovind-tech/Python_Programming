# l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# f=filter(lambda x: x%3==0,l1)
# l2=list(f)
# print(l2)


# l1=[1,2,3,4,5]
# l2=list(map(lambda x: -x,l1))
# print(l2)

# l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# k=lambda x: x if x%2==0 else -x
# l2=list(map(k,l1))
# print(l2)

l1=[[4,2,'six'],[1,4,'five'],[2,2,'four']]

l2=sorted(l1,key=lambda x:x[0]+x[1])

print(l2)