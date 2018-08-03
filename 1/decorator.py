import functools
def log(*text):
	def decorator(func):
		@functools.wraps(func)#now.__name__ is now
		def wrapper(*args,**kw):
			print("%s =%s():" %(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log("execute")
def now():
	print("2018-01-17")
print(now.__name__)#wrapper

