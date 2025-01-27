num = int(input("Enter a number:- "))
tar = int(input("Enter a number:- "))

fact = set()
for i in range(1, num//2+1):
    if num % i == 0:
        fact.add(i)
        fact.add(num//i)
if tar in fact:
    print(tar, "is a factor of", num)
else:
    print(tar, "is not a factor of", num)
# print(fact)

