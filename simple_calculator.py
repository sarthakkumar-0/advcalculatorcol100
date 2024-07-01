from stack import Stack
class SimpleCalculator:
    def __init__(self):
        self.hist=Stack()
        
    def evaluate_expression(self,input_expression):
        """
		Evaluate the input expression and return the output as a float
		Return a string "Error" if the expression is invalid
		"""
        operators=['+','-','*','/']
        def strip_spaces(s):
            a=""
            for i in s:
                if i!=" ":
                    a=a+i
            return a
        final=strip_spaces(input_expression)
        try:
            for i in range(len(final)):
                if final[i] in operators:
                    a=final[:i]
                    b=final[i+1:]
                    c=final[i]
                    break
            v=self.op(int(a),int(b),c)
            self.hist.push((input_expression,v))
            return v
        except:
            v="Error"
            self.hist.push((input_expression,v))
            return v
    def op(self,a,c,oper):
        if oper=='+':
            return float(a+c)
        elif oper=="-":
            return float(a-c)
        elif oper=="*":
            return float(a*c)
        elif oper=="/":
            return a/c
    def get_history(self):
        a=[]
        for i in range(self.hist.__len__()):
            a.append(self.hist.get(i))
        return a

# calculator = SimpleCalculator()
# answer = calculator.evaluate_expression("2 + 3") # answer should be 5.0
# print(answer)
# answer = calculator.evaluate_expression("69        *   89") # answer should be "Error"
# history = calculator.get_history() # history should be [("2 +", "Error"), ("2 + 3", 5.0)]
# print(answer)
# print(history)
# # print(type(history))