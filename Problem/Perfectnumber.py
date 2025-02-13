num = int(input("Enter a number:- "))
temp = 0

for i in range(1, num):
    if num % i == 0:
        temp += i
if num == temp:
    print(num,"is a perfect number")

else:
    print(num,"is not a perfect number")