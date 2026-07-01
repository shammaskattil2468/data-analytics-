num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
chose = input("for mul, for add, for sub: ")

if chose == "add":
    print("answer is", num1 + num2)
elif chose == "mul":
    print("answer is", num1 * num2)
elif chose == "sub":
    print("answer is", num1 - num2)
else:
    print("invalid")
