class Bank:
    apr=1.2
    
ac1=Bank()
print(ac1.apr)
ac2=Bank()
print('dictionary of instance ac2',ac2.__dict__)
# but when the attribute for ac2 is called it refers fiirst to instance dictionary and if it does not find then 
#it goes to class dictionary

print(ac2.apr)
ac3=Bank()
ac3.apr=2.3
print('dictionary of instance ac3',ac3.__dict__)
ac3.Branch='Habsiguda'

print(ac3.__dict__)

print(Bank.__dict__)
print(ac3.__dict__)
"""
The type of class .__dict__ is mapping proxy where as obj.__dict__ is regular dictionary hence in obj__dict __ we can add values
"""
print(type(Bank.__dict__))

print(type(ac3.__dict__))