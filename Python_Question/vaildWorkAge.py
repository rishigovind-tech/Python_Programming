class InvalidAgeError(Exception):
    pass

def validate_age(age):
  
    if age>=18 and age<=60:
        return True
    else:
        raise InvalidAgeError('Age should be between be between 18-60')
    
    

name = 'John Doe'
age = 65  

try:
    validate_age(age)
    print("You can join Work")
except InvalidAgeError as e:
    print(e)  