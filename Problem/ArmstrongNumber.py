num = int(input("Enter a number:- "))



for j in range(1, num+1):
    temp = 0
    str1 = str(j)
    for i in range(len(str1)):

        temp += (int(str1[i]) ** len(str1))
        # print(temp)

    if j == temp:
        print(j, end=" ")
    # else:
    #     print(j,"is not an armstrong number.")