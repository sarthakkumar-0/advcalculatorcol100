from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
	def __init__(self):
		"""
		Call super().__init__()
		Instantiate any additional data attributes
		"""
		super().__init__()

	def evaluate_expression(self, input_expression):
		"""
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
		aa=self.tokenize(input_expression)
		output=self.evaluate_list_tokens(aa)
		self.hist.push((input_expression,output))
		return output



	# def tokenize(self, input_expression):
	# 	"""
	# 	convert the input string expression to tokens, and return this list
	# 	Each token is either an integer operand or a character operator or bracket
	# 	"""
	# 	list_tokens=[]
	# 	def is_number(s):
	# 		try:
	# 			int(s)
	# 			return True
	# 		except:
	# 			return False
	# 	i=0
	# 	# input_expression="("+input_expression+")"
	def tokenize(self, expression):
		tokens = []
		current_token = ""

		for char in expression:
			if char.isdigit():
				current_token += char
			else:
				if current_token:
					tokens.append(int(current_token))
					current_token = ""
				if not char.isspace():
					tokens.append(char)

		if current_token:
			tokens.append(int(current_token))
		return tokens


	def check_brackets(self, list_tokens):
		s=Stack()
		val=True
		for i in list_tokens:
			if(i=='('):
				s.push(i)
			elif(i=='{'):
				if(s.peek()=='('):
					val=False
					break
				else:
					s.push(i)
			elif(i==')'):
				if(s.peek()!='('):
					val=False
					break
				else:
					s.pop()
			elif(i=='}'):
				if(s.peek()!='{'):
					val=False
					break
				else:
					s.pop()
			elif(i=='[' or i==']'):
				val=False
				break
		if(s.is_empty()==False):
			val=False
		return val

	def simple_calc(self,opr,a,c):
		if opr=="+":
			return round(float(a+c),2)
		elif opr=="-":
			return round(float(a-c),2)
		elif opr=="*":
			return round(float(a*c),2)
		elif opr=="/":
			return round(float(a/c),2)

	def evaluate_list_tokens(self,tokens):
		oper=["/","*","+","-"]
		open_brackets=["(","{","["]
		close_brackets=[")","}","]"]
			
		def is_number(s):
			try:
				int(s)
				return True
			except:
				return False
		def prec(i):
			if i=="+":
				return 0
			elif i=="-":
				return 1
			elif i=="*":
				return 2
			elif i=="/":
				return 3
		if self.check_brackets(tokens)==False:
			return "Error"
		def is_correct(tokens):
			check_tokens=tokens.copy()
			i=0
			while i+1<=len(check_tokens):
				if check_tokens[i] in open_brackets:
					check_tokens.pop(i)
				elif check_tokens[i] in close_brackets:
					check_tokens.pop(i)
				else:
					i+=1
			i=0
			for j in check_tokens:
				if i==0 or i==1:
					if is_number(j):
						i+=1
					else:
						i-=1
				else:
					return False	
			if i==1:
				return True
			else:
				return False
		if is_correct(tokens)==False:
			return "Error"
		tokens=["{"]+tokens+["}"]
		operators=Stack()
		operands=Stack()
		for i in tokens:
			if i in open_brackets:
				operators.push(i)
			elif is_number(i):
				operands.push(i)
			elif i in oper:
				if operators.peek() in oper:
					if prec(operators.peek())>prec(i):
						c=operands.peek()
						operands.pop()
						a=operands.peek()
						operands.pop()
						opr=operators.peek()
						operators.pop()
						operands.push(self.simple_calc(opr,a,c))
						operators.push(i)
					else:
						operators.push(i)
				else:
					operators.push(i)
			elif i in close_brackets:
				while operators.peek() in oper:
					c=operands.peek()
					operands.pop()
					a=operands.peek()
					operands.pop()
					opr=operators.peek()
					operators.pop()
					operands.push(self.simple_calc(opr,a,c))
				operators.pop()
		if operators.__len__()==0 and operands.__len__()==1:
			return operands.peek()
		else:
			return "Error"

	def get_history(self):
		"""
		Return history of expressions evaluated as a list of (expression, output) tuples
		The order is such that the most recently evaluated expression appears first 
		"""
		a=[]
		for i in range(self.hist.__len__()):
			a.append(self.hist.get(i))
		return a
calculator = AdvancedCalculator()
# answer = calculator.evaluate_expression("2 + {3 - (4 * 2 + 1)}") # answer should be 2.75
# print(answer)
# answer = calculator.evaluate_expression("2+3/2+1") # answer should be "Error"
# print(answer)
tokens = calculator.tokenize("2+()+3") # tokens should be [2, '+', 3]
print(tokens)
# answer = calculator.evaluate_list_tokens([2, '+', 3]) # answer should be 5.0
# correct_brackets = calculator.check_brackets(['(', 2, '*',')']) # should be False
# print(correct_brackets)
# history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + (3 /4)", 2.75)]
# print(history)

# tokens = calculator.tokenize("2 + 3 *6 /2") # tokens should be [2, '+', 3]
# print(tokens)
answer = calculator.evaluate_list_tokens(tokens) # answer should be 5.0               # error throw
print(answer)

# ["2+()+3","(2+)+3","(2+)3"]