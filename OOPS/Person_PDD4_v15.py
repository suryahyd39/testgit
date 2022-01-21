class Person:
    def say_hello(self):
        print(f'{self} says hello') 

print(Person.say_hello)
print()
print()
p=Person()
p.say_hello()
m1=p.say_hello
print('******')
print(m1.__func__)

"""
below example of monkey patching using lambda expression to define a method at runtime
"""

class people:
    def say_hi(self):
        print(f'instance method called from {self}')
        

people.do_work=lambda self:f'do the work assigned by {self}'


print(people.__dict__)

p2=people()
print(p2.do_work)
print(p2.do_work())