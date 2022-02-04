from datetime import timedelta
from multiprocessing.sharedctypes import Value
import numbers
import datetime as dt

class timeZone:
    def __init__(self,name,offset_hrs,offset_min):
        if name  is None  or len(str(name).strip())==0:
            raise ValueError('Name cannot be empty ')
        if offset_hrs>12 and offset_hrs<-12:
            raise ValueError('offset hrs cannot be greater than 12 or less than -12')
        if offset_min>59 and offset_min<-59:
            raise ValueError('Offset min cannont be greater than 59 or Offset min cannot be less than -59')
        self._name=str(name).strip()
        
        if not isinstance(offset_hrs,numbers.Integral):
            raise ValueError('offset_hrs has to be Integer')
         
        if not isinstance(offset_min,numbers.Integral):
            raise ValueError('offset_min has to be Integer')
        
        offset=timedelta(hours=offset_hrs,minutes=offset_min)
        if offset<timedelta(hours=-12,minutes=0) or offset>timedelta(hours=14,minutes=0):
            raise ValueError('offset has to be between -14 and 12')
        self._offset_hrs=offset_hrs
        self._offset_min=offset_min
        self._offset=offset
        
    @property
    def offset(self):
        return self._offset
    @property
    def name(self):
        return self._name
    def __eq__(self, other):
        return (isinstance(other,timeZone) and self._offset_hrs==other._offset_hrs 
                and self._offset_min==other._offset_min)
        
t=timeZone('MytimeZone',-7,-15)
current=dt.datetime.utcnow()
print(current)
print(current+t.offset)