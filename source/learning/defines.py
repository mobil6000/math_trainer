ARITHMETIC_OPERATORS = {
	'+': (2, 
		lambda a, b: a + b), 
	'-': (2, 
		lambda a, b: a - b), 
	'*': (1, 
		lambda a, b: a * b), 
	'/': (1, 
		lambda a, b: a // b if isinstance(a, int) and isinstance(b, int) else a / b)
}
