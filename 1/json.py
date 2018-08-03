import json
d = dict(name='Bob', age=20, score=88)
data = json.dumps(d)
print(data)
reborn = json.loads(data)
print(reborn)
class Student(object):
	def __int__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score
	def __str__(self):
		return 'Student object (%s,%s,%s)'%(self.name, self.age, self.score)
s = Student('Bob', 20, 88)
std_data = json.dumps(s, default = lambda obj: obj.__dict__)
print('dump Student:', std_data)
reborn = json.loads(std_data, object_hook=lambda d: Student(d['name'], d['age'], d['score']))
print(reborn)