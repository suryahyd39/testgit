class school:
    subject='English'
    def say_hello(self):
        return f'I am learning {self.subject}'
    def say_hi():
        print('Hi This is callable attribute')

s1=school()
output1=s1.say_hello()
print(output1)

s2=school()
s2.subject='French'
output2=s2.say_hello()
print(output2)

print(school.say_hi())