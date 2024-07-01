class Stack:
	def __init__(self):
		# Initialise the stack's data attributes
		self.items=[]
	
	def push(self, item):
		# Push an item to the stack
		self.items.insert(0,item)

	def peek(self):
		# Return the element at the top of the stack
		# Return a string "Error" if stack is empty

		if self.is_empty():
			return "Error"
		else:
			return self.items[0]
	def pop(self):
		# Pop an item from the stack if non-empty
		if self.is_empty():
			return "Error"
		else:
			self.items.pop(0)

	def is_empty(self):
		# Return True if stack is empty, False otherwise
		return len(self.items)==0

	def __str__(self):
		# Return a string containing elements of current stack in top-to-bottom order, separated by spaces
		# Example, if we push "2" and then "3" to the stack (and don't pop any elements), 
		# then the string returned should be "3 2"
		
		result=""
		for i in range(len(self.items)):
			if i==0:
				result=result + str(self.items[0])
			else:
				result =result + " " + str(self.items[i])
		return result	
  
		# result=[]
		# for i in range(len(self.items)):
		# 	result.append(self.items[i])
		# return result

	def __len__(self):
		# Return current number of elements in the stack
		return len(self.items)
	def get(self,i):
		return self.items[i]