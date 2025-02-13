n = int(input("Enter a number:- "))
num1 = 0
num2 = 1
# ans = [0, 1]

print(num1, num2, end=" ")
for i in range(n-2):

    next = num1 + num2
    num1 = num2
    num2 = next
    print(next, end=" ")

