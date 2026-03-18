# # Reverse a Number

# n =1257 
# rev=0

# while n>0:
#     r=n%10
#     rev=rev*10 + r
#     n=n//10
#     print(rev)
    
    
#palindrome

# n= int(input("Enter the number: "))
# rev=0
# m=n

# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
    
# print(rev)
    
# if rev==m:
#     print("its palindrome")
# else:
#     print("not a palindrome")


#n number

# n=5
# i=1
# sum=0
# print('Enter',n,"Numbers")

# while i<=n:
#     x=int(input())
#     sum += x
#     i=i+1

# print("Sum =",sum)

#Max Element

# n=5
# print("Enter 5 number")
# i=0
# max= float('-inf')
# min= float('inf')
# while i<n:
#     i=i+1
#     x=int(input())
#     if x>max:
#         max=x
#     if x < min:
#         min=x

# print('Max Elements', max) 
# print('Min Elements', min)

# Fibonacci

# n=int(input('Enter a Number'))
# a=0
# b=1
# for i in range(0,n):
#     c=a+b
#     a=b
#     b=c
# print(a)
 
#  Factors of a number

# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     if n % i ==0:
#         print("Factors of ", n , "is : ", i )
        

#Prime Number

# n = int(input("Enter the number : "))
# count=0

# for i in range(1,n+1):
#     if n % i ==0:
#         count+=1
# if count ==2:
#     print("it is prime")
# else:
#     print("it is not prime")




    # prime number 1-100
    
# for n in range (1,101):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count +=1
#     if count ==2:
#         print(n)


# Patterns

for i in range(1,6):
    for j in range(1,6):
        print("*",end='')
    print('')
    
    
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end='')
    print('')
        
        
        
        
    

