class Student(object):
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self,value):
		self._age=value
	@property
	def sex(self):
		return 1
s=Student()
s.age=2
print(s.age)
print(s.sex)
print(Student.age)
print(Student.sex)