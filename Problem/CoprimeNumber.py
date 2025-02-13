num1 = int(input("Enter first number:- "))
num2 = int(input("Enter second number:- "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(2, num1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        print("Numbers are not coprime")
        break
else:
    print("Numbers are coprime")
