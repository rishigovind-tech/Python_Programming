# ----------FUNCTION-----------------

# def calc_sum(a,b):
#     sum =a+b
#     print(sum)
#     return sum
    

# calc_sum(10,5)
# calc_sum(40,85)

#Avaerage of three numbers

# def avg(a,b,c):
#     sum=a+b+c
#     average=sum/3
#     print(average)
#     return average

# avg(10,20,30)

#PRACTICE

#length of a list

# city=["delhi","bangalore","nodia","kochi","mumbai","chennai"]
# bike=["hunter","bullet","classic","rx100","activa"]

# def printlen(list):
#     print(len(list))
    
    
# printlen(city)
# printlen(bike)

#elements of a list in single line

# city=["delhi","bangalore","nodia","kochi","mumbai","chennai"]
# bike=["hunter","bullet","classic","rx100","activa"]

# def  printele(list):
    
#     for i in list:
#         print(i,end=" ")
        
# printele(city)
# print("\n")
# printele(bike)

#factorial

# number = int(input("Enter the number: "))

# def factorial(num):
#     fact=1
#     n=1
#     while n<=num:
#         fact *=n
#         n+=1
#     print(fact)
#     return fact

# factorial(number)

#convert USD to INR

# usd= int(input("Enter the amount to convert : "))

# def convertor(amount):
#     inr=83
#     amountINR=amount*inr
#     print(amountINR)
#     return amountINR

# convertor(usd)





# RECURSION

def show(n):
    if (n==0):
        return
    print(n)
    show(n-1)
    
show(5)
        
        

