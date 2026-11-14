class Debt:
    def __init__(self, name, amount_borrowed):
        self.name = name
        self.amount_borrowed = amount_borrowed
        self.amount_paid = 0
    def make_payment(self, amount):
        if amount <= 0:
            print("Amount can't be zero or negative")
            return
        if amount > self.balance():
            print("Amount you are trying to pay exceeds the amount you owe")
            return
        self.amount_paid += amount 
    def is_cleared(self):
        return self.amount_paid >= self.amount_borrowed 
    def balance(self):
        return self.amount_borrowed - self.amount_paid
    def summary(self):
        print(f"{self.name} borrowed {self.amount_borrowed } and his balance is {self.balance()}")
        if self.is_cleared():
            print(f"{name} DEBT IS CLEARED")
        else:
            print(f"{name} IS STILL OWING")
name = input("Who did you lend money: ")
while True:
    try:
        amount_borrowed = int(input(f"How much did you lend {name} : "))
    except ValueError:
        print("Amount borrowed can't be letters")
    else:
        print(f"{name} borrowed {amount_borrowed}")
        break
debt = Debt(name, amount_borrowed)
while not debt.is_cleared():
    while True:
        try:
            amount = int(input(f"How much {name} deposit: "))
        except ValueError:
            print("Amount paid can't be letters")
        else:
            print(f"{name} borrowed {amount_borrowed} and deposited {amount}")
            break 
    debt.make_payment(amount)
    print(f"{name} deposited {amount}")
    print(f"{name}'s balance is {debt.balance()}")
debt.summary()