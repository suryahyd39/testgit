class TransactionID:
    def __init__(self,start_id):
        self._start_id=start_id
    def nextval(self):
        self._start_id+=1
        return self._start_id
    
class Account:
    Transaction_Number=TransactionID(100)
    def give_next(self):
        next_val=Account.Transaction_Number.nextval()
        return next_val
    
a1=Account()
a2=Account()
a3=Account()
print(a1.give_next())
print(a2.give_next())
print(a3.give_next())