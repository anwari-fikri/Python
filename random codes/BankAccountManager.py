class Account:
    # Define an __init__ constructor method with attributes shared by all accounts:
    def __init__(self,acc_num,opening_deposit):
        self.acc_num = acc_num
        self.balance = opening_deposit
    
    # Define a __str__ mehthod to return a recognizable string to any print() command
    def __str__(self):
        return f'${self.balance:.2f}'
    
    # Define a universal method to accept deposits
    def deposit(self,dep_amt):
        self.balance += dep_amt

    # Define a universal method to handle withdrawals
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            print('Funds Unavailable')  # changed "return" to "print"

class Checking(Account):
    def __init__(self,acc_num,opening_deposit):
        super().__init__(acc_num,opening_deposit)
    
    def __str__(self):
        return f'Checking Account #{self.acc_num}\n  Balance: {Account.__str__(self)}'

    
class Savings(Account):
    def __init__(self,acc_num,opening_deposit):
        super().__init__(acc_num,opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.acc_num}\n  Balance: {Account.__str__(self)}'


class Business(Account):
    def __init__(self,acc_num,opening_deposit):
        super().__init__(acc_num,opening_deposit)

    def __str__(self):
        return f'Business Account #{self.acc_num}\n  Balance: {Account.__str__(self)}'

class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        
        # Create a dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C':[],'S':[],'B':[]}
        
    def __str__(self):
        return self.name
        
    def open_checking(self,acc_num,opening_deposit):
        self.accts['C'].append(Checking(acc_num,opening_deposit))
    
    def open_savings(self,acc_num,opening_deposit):
        self.accts['S'].append(Savings(acc_num,opening_deposit))
        
    def open_business(self,acc_num,opening_deposit):
        self.accts['B'].append(Business(acc_num,opening_deposit))
    
    # rather than maintain a running total of deposit balances,
    # write a method that computes a total as needed
    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total:.2f}')

def make_dep(cust,acct_type,acc_num,dep_amt):
    """
    make_dep(cust, acct_type, acc_num, dep_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acc_num  = integer
    dep_amt   = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acc_num == acc_num:
            acct.deposit(dep_amt)
        
def make_wd(cust,acct_type,acc_num,wd_amt):
    """
    make_dep(cust, acct_type, acc_num, wd_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acc_num  = integer
    wd_amt    = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acc_num == acc_num:
            acct.withdraw(wd_amt)

x = Savings(54321,654.33)
print(x)
x.withdraw(1000)
x.withdraw(30)
x.balance

print()
bob = Customer('Bob',1)
bob.open_checking(321,555.55)
bob.get_total_deposits()
bob.open_savings(564,444.66)
bob.get_total_deposits()

print()
nancy = Customer('Nancy',2)
nancy.open_business(2018,8900)
nancy.get_total_deposits()

print()
make_dep(nancy,'B',2018,67.45)
nancy.get_total_deposits()
make_wd(nancy,'B',2018,1000000)
nancy.get_total_deposits()

print()
nancy = Customer('Nancy',2)
nancy.open_business(2018,8900)
nancy.get_total_deposits()
make_wd(nancy,'B',2018,1000000)
nancy.get_total_deposits()