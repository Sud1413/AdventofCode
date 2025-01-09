f = open("input.txt", "r")
lines = f.readlines()
dict1 = {}
set1 = set()

row1, col1, row2, col2 = 0, 0, 0, 0
# dict1[(row1, col1)] = 1
# set1.add((row2, col2))

for i in lines:
    for line in range(0, len(i), 2):
        if i[line] == ">":
            col1 += 1
        elif i[line] == "<":
            col1-= 1
        elif i[line] == "^":
            row1 += 1
        elif i[line] == "v":
            row1 -= 1
        # if (row1, col1) in dict1:
        #     dict1[(row1, col1)] += 1
        # if (row1, col1) not in dict1:
        #     dict1[(row1, col1)] = 1
        set1.add((row1, col1))
        # print(i[line])

    for l in range(1, len(i), 2):
        if i[l] == ">":
            col2 += 1
        elif i[l] == "<":
            col2 -= 1
        elif i[l] == "^":
            row2 += 1
        elif i[l] == "v":
            row2 -= 1
        # if (row2, col2) in dict1:
        #     dict1[(row2, col2)] += 1
        # if (row2, col2) not in dict1:
        #     dict1[(row2, col2)] = 1
        set1.add((row2, col2))


# print(len(dict1))
print(len(set1))

