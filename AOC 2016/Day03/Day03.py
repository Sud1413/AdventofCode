f = open("input.txt", "r")
lines = f.readlines()

ans = 0
a = []
b = []
c = []

# for line in lines:
#     a, b, c =map(int, line.split())
#
#     if (a + b > c) and (a + c > b) and (c + b > a):
#         ans += 1
#     # print(line, type(line), l1)
#
# print(ans)

for line in lines:
    x, y, z = map(int, line.split())
    a.append(x)
    b.append(y)
    c.append(z)

for i in range(0, len(a)-2,3):
    if (a[i] + a[i+1] > a[i+2]) and (a[i] + a[i+2] > a[i+1]) and (a[i+1] + a[i+2] > a[i]):
        ans += 1
        # print(ans, end=" ")
    if (b[i] + b[i+1] > b[i+2]) and (b[i] + b[i+2] > b[i+1]) and (b[i+1] + b[i+2] >b[i]):
        ans += 1

    if (c[i] + c[i+1] > c[i+2]) and (c[i] + c[i+2] > c[i+1]) and (c[i+1] + c[i+2] >c[i]):
        ans += 1



print(ans)
