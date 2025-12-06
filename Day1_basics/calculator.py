A=float(input(  "Enter first number: ")) 
B=float(input(  "Enter second number: ")) 

operatiions = input("Enter operation (+, -, *, /): ")

if operatiions == '+':      
    result = A + B
    print("Result:", result)
elif operatiions == '-':
    result = A - B
    print("Result:", result)    
elif operatiions == '*':
    result = A * B
    print("Result:", result)        
elif operatiions == '/':
    if B != 0:
        result = A / B
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")