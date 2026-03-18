# a,b=10,0

# try:
#     c=a//b
#     print(c)
# except:
#     print('error')
        
# print('end')

# L=[10,20,30,40,50,60]
# print(L)

# try:
#     index =int(input('Enter a index to find element : '))
#     print(L[index])
    
# except:
#     print("Enter a vaild index")

# print('End of Program')


# ===========================Multiple Exception================================


L=[10,20,30,40,50,60]
print(L)

try:
    index =int(input('Enter a index to find element : '))
    print(L[index])
    
except IndexError:
    print("Error!!!...Enter a vaild index")
except ValueError:
    print("Error!!!...Input should be a int")
except TypeError:
    print("Error!!!...Input should be a int")
except:
    print("Error!!!...")
    

print('End of Program')
