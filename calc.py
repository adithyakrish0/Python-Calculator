def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "❌ Error: Cannot divide by zero!"
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def display_menu():
    print("\n🧮 Python CLI Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

while True:
    display_menu()
    choice = input("Choose an operation (1-7): ")

    if choice == '7':
        print("👋 Exiting Calculator. Goodbye!")
        break

    if choice not in ['1','2','3','4','5','6']:
        print("⚠️ Invalid choice. Please select from 1 to 7.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("⚠️ Invalid input. Please enter numbers only.")
        continue

    if choice == '1':
        result = add(num1, num2)
        op = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        op = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        op = '*'
    elif choice == '4':
        result = divide(num1, num2)
        op = '/'
    elif choice == '5':
        result = modulus(num1, num2)
        op = '%'
    elif choice == '6':
        result = power(num1, num2)
        op = '**'

    print(f"✅ Result of {num1} {op} {num2} = {result}")
