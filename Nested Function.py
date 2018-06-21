def raise_val(n):
	'''resturn the n raise'''
	def inner(x):
		return x**n
	return inner
square=raise_val(2)
cube= raise_val(3)
print(square(10),cube(6))
