f = open("input.txt","r")

lines = f.readlines()
count, ans = 0, 1
for line in lines:
    for i in range(len(line)):
        if line[i] == "(":
            count+= 1
        elif line[i] == ")":
            count-= 1
        if count == -1:
            ans = i
            break
print(ans)
