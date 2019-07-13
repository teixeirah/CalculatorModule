import sys
class Calculator:
	def __init__(self, st_msg, nd_msg, rd_message, fourth_msg, fifth_msg, sixth_msg):
		self.op = None
		self.res = None
		self.num1 = None
		self.num2 = None
		self.res_msg = None
		self.num1_msg = None
		self.num2_msg = None
		self.st_msg = st_msg
		self.nd_msg = nd_msg
		self.rd_msg = rd_message
		self.fourth_msg = fourth_msg
		self.fifth_msg = fifth_msg
		self.sixth_msg = sixth_msg

	def welcome(self):
		print(self.st_msg)
		print(self.nd_msg)
		print(self.rd_msg)
		print(self.fourth_msg)
		print(self.fifth_msg)
		print(self.sixth_msg)

	def op_input(self):
		self.op = str(input("-> "))
		if self.op == "+":
			print("Operation -> Addition")
			self.num1_msg = "->Type the first number of you'r adition"
			print(self.num1_msg)
			self.num1 = float(input("--> "))
			self.num2_msg = "Type the number that you want to add " + str(self.num1)
			print(self.num2_msg)
			self.num2 = float(input("--> "))
			self.res = self.num1 + self.num2
			self.res_msg = str(self.num1) + " plus " + str(self.num2) + " is equal to: " + str(self.res)
			print(self.res_msg)

		if self.op == "-":
			print("Operation -> Subtracting")
			self.num1_msg = "->Type the first number of you'r subtraction"
			print(self.num1_msg)
			self.num1 = float(input("--> "))
			self.num2_msg = "Type the number that you want to subtract by " + str(self.num1)
			print(self.num2_msg)
			self.num2 = float(input("--> "))
			self.res = self.num1 - self.num2
			self.res_msg = str(self.num1) + " minus " + str(self.num2) + " is equal to: " + str(self.res)
			print(self.res_msg)

		if self.op == "*":
			print("Operation -> Multiplication")
			self.num1_msg = "->Type the first number of you'r multiplication"
			print(self.num1_msg)
			self.num1 = float(input("--> "))
			self.num2_msg = "Type the number that you want to multiply by " + str(self.num1)
			print(self.num2_msg)
			self.num2 = float(input("--> "))
			self.res = self.num1 * self.num2
			self.res_msg = str(self.num1) + " times " + str(self.num2) + " is equal to: " + str(self.res)
			print(self.res_msg)

		if self.op == "/":
			print("Operation --> Division")
			self.num1_msg = "->Type the first number of you'r division"
			print(self.num1_msg)
			self.num1 = float(input("--> "))
			self.num2_msg = "Type the number that you want to divide by " + str(self.num1)
			print(self.num2_msg)
			self.num2 = float(input("--> "))
			self.res = self.num1 / self.num2
			self.res_msg = "-> " + str(self.num1) + " divided by " + str(self.num2) + " is equal to: " + str(self.res)
			print(self.res_msg)

		if self.op == "off":
			sys.exit(0)
