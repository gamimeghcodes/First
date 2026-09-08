balance = 1000.0  


def withdraw(amount):
    global balance

    if amount <= 0:
        print("Error: Withdrawal amount must be greater than zero.")
    elif amount > balance:
        print(f" Error: Insufficient funds. Your balance is ${balance}.")
    else:
        balance -= amount
        print(f" Successfully withdrew ${amount}.")
        print(f" Remaining balance: ${balance}.")


print(f"Starting Balance: ${balance}")
withdraw(300)  
withdraw(800)
