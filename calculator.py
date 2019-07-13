from calc_module import Calculator

calc = Calculator("\nTHIS-IS-A-CALCULATOR", "-> Type '+' to add '2' numbers", "-> Type '-' to subtract '2' numbers", "-> Type '*' to multiply '2' numbers", "-> Type '/' to divide '2' numbers", "-> Type 'off' to turn-off the calculator")
while True:
	calc.welcome()
	calc.op_input()

