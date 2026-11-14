# Let's create a plan that many debt books can be drawn from
class Debt:
# Now the object;the builders instructions of the book being built
    def __init__(self, name, amount_borrowed):
# Now the permanent details 
        self.name = name
        self.amount_borrowed = amount_borrowed
        self.amount_paid = 0
# Now the method the action of the book
    def make_payment(self, amount):
        if amount <= 0:
            print("Amount can't be zero or negative'")
            return 
        if amount > self.amount_borrowed - self.amount_paid:
            print("The amount you are trying to pay exceeds the amount owed")
            return 
        self.amount_paid += amount
    def is_cleared(self):
        if self.amount_paid >= self.amount_borrowed:
            return True 
        else:
            return False 
    def balance(self):
       return self.amount_borrowed - self.amount_paid
    def summary(self):    
       print(f"{self.name} borrowed {self.amount_borrowed} and balance is {self.balance()}")
       if self.is_cleared():
           print("CLEARED")
       else:
           print("OWING")
d = Debt("Claude", 3000)
d.make_payment(2000)
print(d.amount_paid) 
d.make_payment(1500)
print(d.amount_paid)
print(f"{d.name} is owing {d.amount_borrowed - d.amount_paid}")
a = Debt("Grok", 4000)
a.make_payment(1200)
a.make_payment(2800)
print(a.amount_paid)
print(f"{a.name} is owing {a.amount_borrowed - a.amount_paid}")
print(f"Claude paid {d.amount_paid}")
print(f"Grok paid {a.amount_paid}")
print(d.is_cleared())
print(a.is_cleared() )
print(d.balance())
print(a.balance())
a.summary()
d.summary()
b = Debt("Gemini", 2000)
b.make_payment(1000)
b.make_payment(1000)
b.make_payment(-400)
print(b.is_cleared())
b.summary()