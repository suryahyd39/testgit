from distutils.log import info
import random
class school:
    def __init__(self,name,location):
        self._name=name
        self._location=location
    @property
    def getLoc(self):
        return self._location
    @getLoc.setter
    def getLoc(self,loc):         
        self._location=loc
    def provide_application(self,amount_paid):
        self.amount_paid=amount_paid
        return True  if self.amount_paid ==200 else False   
    
    
    def admission(self,):
        if self.provide_application:
            return True
        else:
            return False
    
    def providAdmitCard(self):
        if self.admission:
            self.admitNo=random.randint(100000,999999)
        return self.admitNo
    

jbm=school('JBM','VDN')
information=jbm.getLoc
print(information)
jbm.getLoc='BLR'
information=jbm.getLoc
print(information)