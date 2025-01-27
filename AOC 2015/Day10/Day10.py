f = open("input.txt", "r")

line = f.readlines()
str1 = str(line)

# str1 = str(1321131112)

def problem(str1):
   add = 0
   ans = ""
   curr = 0
   next = curr

   while curr <= len(str1) and next < len(str1):
       if str1[curr] == str1[next]:
           add += 1
           next += 1
       else:
           ans += str(add)
           ans += str(str1[curr])
           add = 0
           curr = next
   # print(ans)
   add = 1
   for i in range(len(str1)-1,1, -1):
       if str1[i] == str1[i-1]:
           add += 1
       else:
           ans += str(add)
           ans += str(str1[i])
           break
   return ans

print(problem(str(1321131112)))


for i in range(1, 51):
    str1 = problem(str1)
    print(len(str1), i)


