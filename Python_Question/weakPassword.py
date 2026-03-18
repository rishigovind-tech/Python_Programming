class WeakPasswordError(Exception):
    pass

def is_strong(password):
    
    msg = 'Password must contain at least '
    
    if len(password) < 8:
        return WeakPasswordError(msg + "8 characters.")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = set("!@#$%^&*-_+=")
    has_special = any(c in special_chars for c in password)

    if not has_upper:
        return WeakPasswordError( msg + "one uppercase letter.")
    if not has_lower:
        return WeakPasswordError( msg + "one lowercase letter.")
    if not has_digit:
        return WeakPasswordError( msg + "one digit.")
    if not has_special:
        return WeakPasswordError( msg + "one special char (!@#$%^&*-_+=).")

    return True, "Password is strong!"

    


pwd = is_strong("admin#123Net")
print(pwd)
