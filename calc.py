
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the Operator(+ - * /): ")
if operator == "+":
    result=num1+num2
elif operator == "-":
    result=num1-num2
elif operator=="*":
    result=num1*num2
elif operator=="/":
    if num2 == 0:
        print("Error: Division by 0 is not possible")
    else:
        result=num1/num2    

print(f"Result= {result:.2f}")



