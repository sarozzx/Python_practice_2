# Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

class Calculator:
    def __init__(self,num1,num2,oper):
        try:
            self.number1=int(num1)
            self.number2=int(num2)
        except ValueError:
            raise ValueError("Enter integers :")
        self.operator=operator
    def calcu(self):
        operators={
            '+': self.add(),
            '-': self.subtract(),
            '*': self.multiply(),
            '/': self.divide()
        }
        return operators.get(self.operator)

    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        try:
            result = self.number1 / self.number2
        except ZeroDivisionError:
            result = 0
        return result

x1= input('Enter the first number: ')
x2 = input('Enter the second number: ')
operator = input('Enter the operator (+,-,*,/)')
obj1 = Calculator(x1, x2, operator)
print(obj1.calcu())
