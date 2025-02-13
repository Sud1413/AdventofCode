num = int(input("Enter a number:- "))
ans = set()
for fact in range(1, ((num)//2)+1):
    if num % fact == 0:
        ans.add(fact)
        ans.add(num//fact)


print(ans)