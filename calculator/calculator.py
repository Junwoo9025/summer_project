# calculator practice


#Add
def add(n1, n2):
    return n1 + n2


#Subtract
def subtract(n1, n2):
    return n1 - n2


#Multiply
def multiply(n1, n2):
    return n1 * n2


#Divide
def divide(n1, n2):
    return n1 / n2

#Dictionary

operations = {
 "+": add,
 "-": subtract,
 "*": multiply,
 "/": divide
  }

num1 = int(input("what is your first number?: "))

for symbol in operations:
  print(symbol) 
operation_symbols = input("Pick an operation from the line above: ")
num2 = int(input("what is your second number?: "))

calculation_function = operations[operation_symbols]
answer = calculation_function(num1, num2)
  
print(f"{num1} {operation_symbols} {num2} = {answer}")