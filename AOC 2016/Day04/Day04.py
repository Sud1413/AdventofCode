f = open("input.txt", "r")
lines = f.readlines()

dict1 = {}

for line in lines:
    l1 = line.split("-")
    # l1 = line.split("[")

    print(l1, type(l1))
    for i in line:
        if i in dict1:
            dict1[i] +=1
        else:
            dict1[i] = 1
    print(dict1)
    break
