def calculator(operand1, operand2, operator) :
    if operator == "+" :
        return operand1 + operand2
    if operator == "-" :
        return operand1 - operand2 
    if operator == "*" :
        return operand1 * operand2
    if operator == "/" :
        return operand1 / operand2 

print("provide two numbers for simple arithmetic operation")
operand1 = int(input())
operand2 = int(input())

print("Provide the operation symbol \"+, -, *, /\" that u want to perform on the given operands")
operator = input()

if operator == "+" :
    print("Addition of", operand1 , "and", operand2, "is :", calculator(operand1, operand2, operator))
if operator == "-" :
    print("Subtraction of", operand2 , "from", operand1, "is :", calculator(operand1, operand2, operator))
if operator == "*" :
    print("Multiplication of", operand1 , "and", operand2, "is :", calculator(operand1, operand2, operator))
if operator == "/" :
    print("Division of", operand1 , "and", operand2, "is :", calculator(operand1, operand2, operator))