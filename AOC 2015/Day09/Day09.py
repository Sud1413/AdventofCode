f = open("input.txt", "r")

lines = f.readlines()

dict1 = {}
list1 = []
for line in lines:
    for i,j in range(len(line)):
        if line[i] == "t" and line[i+1] == "o" and line[j] == "=":
            # list1.append(line[0:i])
            # dict1[line[0:i]] = int(line[i+1:])
            dict1[line[0:i-1]] = line[i + 3:j]
    # print(line)

print(dict1)


    # list1 += line.split("to")
    # list1 += line.split("=")
    # dict1[line] = 1
# print(dict1)
# print(list1)