
#                                                 # Area of a Circle
# r = float(input("Enter radius: "))
# area = 3.14 * r * r
# print("Area of the circle =", area)
#                                                 # 2. Area of a Rectangle
# l = float(input("Enter length: "))
# w = float(input("Enter width: "))
# area = l * w
# print("Area of rectangle =", area)
#                                                 # 3. Simple Interest
# p = float(input("Enter principal: "))
# r = float(input("Enter rate: "))
# t = float(input("Enter time: "))
# si = (p * r * t) / 100
# print("Simple Interest =", si)
#                                                 # 4. Square of a Number
# num = int(input("Enter a number: "))
# square = num * num
# print("Square =", square)
#                                                 # 5. Cube of a Number
# num = int(input("Enter a number: "))
# cube = num * num  * num
# print("Cube =", cube)
#                                                 # 6. Perimeter of a Rectangle
# l = float(input("Enter length: "))
# w = float(input("Enter width: "))
# perimeter= 2 * (l + w)
# print("Perimeter =", perimeter)
#                                                 # 7. Average of Three Numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# avg = (a + b + c) / 3
# print("Average =", avg)
#                                                 # 8. Multiplication Table of 5 (for loop)
# for i in range(1, 11):
#     print("5 x", i, "=", 5 * i)
#                                                 # 9. Sum of Numbers up to 100 (for loop)
# sum = 0
# for i in range(1, 101):
#     sum = sum + i

# print("Sum =", sum)
#                                                 # 10. Sum of Even Numbers up to n
num = int(input("Enter the number: "))
sum = 0

for i in range(2, num+1, 2):
    sum = sum + i
print("Sum  =", sum)