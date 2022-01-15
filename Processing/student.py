class student:
	"""
	the student class is developed by Surya"""
	def __init__(self):
		print('studentid' ,id(self))
		self.name='Surya'
		self.rollno=101
		self.marks=90

	def talk(self):
		print('hello i am ',self.name)
		print('my rollno is ',self.rollno)
		print('my marks no is',self.marks)



s1=student()
print(id(s1))
