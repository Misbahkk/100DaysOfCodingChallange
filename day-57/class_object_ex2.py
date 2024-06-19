class Account:
    def __init__(self,blance,account_no):
        self.blance = blance
        self.account_no = account_no

    
    def debit(self,amount):
        self.blance = self.blance - amount

    def credit(self,amount):
        self.blance = self.blance + amount
    
    def print_blance(self):
        print("Your Current Blance is: ",self.blance)

    

bank = Account(2000,325678)
bank.debit(200)
# bank.credit(1000)
bank.print_blance()


    
