"""
the below functions are used to implement through class
import itertools
acct_num=(itertools.count(100))
print(next(acct_num))
print(next(acct_num))
"""
import itertools
class TransactionNumber:
    transaction_counter=itertools.count(100)
     
    def nextval(self):
        self._nextval=next(TransactionNumber.transaction_counter)         
        
        return  self._nextval
    
t=TransactionNumber() 
num=t.nextval()
print(num)
num1=t.nextval()
print(num1)