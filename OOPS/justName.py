class Person:
    def __init__(self):
        self._name=''
    
    @property
    def name(self):
        print('getter called')
        return self._name
    @name.setter
    def name(self,name):
        print('setter called ...')
        if isinstance(name,str) and len(name)>0:
            self._name=name
        else:
            raise ValueError('name cant be empty and has to be alphabetic') 
        
    
p=Person()
p.name='Surya'
print(p.name)
 