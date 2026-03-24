import heapq

H=[]

heapq.heappush(H,20)
heapq.heappush(H,50)
heapq.heappush(H,10)
heapq.heappush(H,30)
heapq.heappush(H,5)
heapq.heappush(H,50)

print(H)

heapq.heappop(H)
print(H)

A=[500, 1, 202, 510, 130, 59]
heapq.heapify(A)
print(A)