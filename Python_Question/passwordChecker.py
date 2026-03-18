
def storng_paaword(password):
    msg = 'Password must contain at least'
    if len(password)<8:
        return False, msg + " 8 characters"
    
    has_upper=any(c.isupper() for c in password)
    has_lower=any(c.islower() for c in password)
    has_digit=any(c.isdigit() for c in password)
    spcl_char=set("!@#$%^&*-_+=")
    has_spcl=any(c in spcl_char for c in password)
    
    if not has_upper:
        return False,msg + " one uppercase letter."
    if not has_lower:
        return False,msg + " one lowercase letter."
    if not has_digit:
        return False,msg + " one digit."
    if not has_spcl:
        return False,msg + " one special char (!@#$%^&*-_+=)"
    
    return True,"Password is strong!!!"


password = input("Enter the password : ")
vaild,message=storng_paaword(password)
print(message)
    
        