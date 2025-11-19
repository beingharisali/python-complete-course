class Account:
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
    def debit(self, amount):
        self.bal -=amount
        print("RS", amount , " was debited")
        print("Now the balance is", self.get_bal())
    def credit(self, amount):
        self.bal +=amount
        print("RS", amount , " was credited")
        print("Now the balance is", self.get_bal())
    def get_bal(self):
        return self.bal

    

# acc1 = Account(10000, 1234)
# acc1.debit(4000)
# acc1.credit(5000)
# print(acc1.get_bal())


acc2 = Account(100000, 4321)
acc2.credit(50000)

acc2.debit(30000)