
class InsuffFundError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsuffFundError("Not enough funds")
    return balance - amount

balance = 5000
amount= int(input("Enter Amount : "))

try:
    balance=withdraw(balance, amount)
    print("Withdrawal successful")
    print("Remaining balance : ", balance)
except InsuffFundError as e:
    print(e)