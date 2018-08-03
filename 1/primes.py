def odd_iter(i):
	n=1
	while i-1>0:
		n=n+2
		i=i-1
		yield n
def not_divisible(n):
    return lambda x:x%n>0
def primes():
	yield 2
	it =odd_iter(10)
	while True:
		n = next(it)
		yield n
		it = filter(not_divisible(n),it)
def main():
	for n in primes():
		print(n)
if __name__=='__main__':
	main()
