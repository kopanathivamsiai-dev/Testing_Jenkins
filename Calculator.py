import sys

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

if len(sys.argv) < 4:
    print("Usage: python Calculator.py <choice> <num1> <num2>")
    sys.exit(1)

choice = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if choice == '1':
    print(num1, "+", num2, "=", (num1 + num2))
elif choice == '2':
    print(num1, "-", num2, "=", (num1 - num2))
elif choice == '3':
    print(num1, "*", num2, "=", (num1 * num2))
elif choice == '4':
    if num2 == 0:
        print("Error: Division by zero")
    else:
        print(num1, "/", num2, "=", (num1 / num2))
else:
    print("Invalid choice")
