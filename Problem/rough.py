from tkinter.font import names

# num = int(input("Enter a number:- "))
# ans = 1

# if num >= 2:
#     for i in range(num, 1, -1):
#         ans *= i
# elif (num==0) or (num == 1):
#     ans = 1
# else:
#     ans = -1
#
# print(ans)


def factorial(num,ans):
    if num == 1:
        # print(ans)
        return ans
    ans *= num
    return factorial(num-1, ans)

if __name__ == "__main__":
    num = int(input("Enter a number:- "))
    ans = 1
    print(factorial(num,ans))
    # factorial(num, ans)

