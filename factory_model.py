# -*-coding:UTF-8-*-
from abc import ABCMeta,abstractmethod

class Operation():
	def __init__(self,NumberA=0,NumberB=0):
		self.NumberA = NumberA
		self.NumberB = NumberB

	def GetResult(self):
		pass

class AddOp(Operation):
	def GetResult(self):
		return self.NumberB + self.NumberA

class MinusOp(Operation):
	def GetResult(self):
		return self.NumberA - self.NumberB

class MultiOp(Operation):
	def GetResult(self):
		return self.NumberA * self.NumberB

class DivideOp(Operation):
	def GetResult(self):
		try:
			return 1.0*self.NumberA / self.NumberB
		except ZeroDivisionError:
			raise

class OperationFatory():
	def ChooseOperation(self,op):
		if op == '+':
			return AddOp()
		if op == '-':
			return MinusOp()
		if op == '*':
			return MultiOp()
		if op == '/':
			return DivideOp()

if __name__ == '__main__':
	ch = ''
	while not ch=='q':
		NumberA = eval(input('Please input number1:  '))
		op = str(input('Please input the operation:  '))
		NumberB = eval(input('Please input number2:  '))
		OPFactory = OperationFatory()
		OPType = OPFactory.ChooseOperation(op)
		OPType.NumberA = NumberA
		OPType.NumberB = NumberB
		print('The result is:',OPType.GetResult())
		print('\n#--  input q to exit any key to continue')
		try:
			ch = str(input())
		except:
			ch = ''