class bank_account:
    acc_holders = {}
    def __init__ (self,account_holder, starting_balance):
        self.balance = starting_balance
        self.accholder = account_holder 
        bank_account.acc_holders[self.accholder] = self
    def deposit(self, amount):
        self.deposit_amount = amount
        self.balance = self.balance + self.deposit_amount
    def withdraw(self, amount):
        self.money_withdrawn = amount
        if self.money_withdrawn <= self.balance:
            self.balance = self.balance - self.money_withdrawn
        else:
            print("You have insufficient money to withdraw")
    def check_balance(self):
        print(self.balance)
    def transfer (self, amount, recipient_name):
        self.trans_amount = amount
        recipient_account= bank_account.acc_holders[recipient_name] 
        if self.trans_amount > self.balance:
            print("You have insufficient funds to do the transfer")
        else:
            self.balance -= self.trans_amount
            recipient_account.balance += self.trans_amount


p = bank_account("Jim Jones", 500)
q = bank_account("Martin Tyler" , 7000)
q.transfer(8000,"Jim Jones")
q.withdraw(8000)
q.check_balance()
p.check_balance()