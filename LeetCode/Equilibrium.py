def findEquilibrium(arr):
    r = sum(arr)
    l = 0

    for equi in range(len(arr) - 1):

        r -= arr[equi]
        if l == r:
            return equi
        l += arr[equi]
        # print("right:- ", r)
        # print("left:- ", l)


    else:
        return -1


if __name__ == "__main__":
    arr = [-7, 1, 5, 2, -4, 3, 0]
    print("equi:- ", findEquilibrium(arr))