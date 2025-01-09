f = open("input.txt", "r")

lines = f.readlines()
l1 = []
ans = 0
ribb = 0
def tsa(l,b,h):
    area = 2*l*b + 2*b*h + 2*h*l
    return area

def slack(l, b, h):
    if h < l:
        h, l = l, h
    if h < b:
        h, b = b, h
    add = (l * b)
    return add

def ribbon(l, b, h):
    if h < l:
        h, l = l, h
    if h < b:
        h, b = b, h
    leng = (2 *(l + b)) + (l*b*h)
    return leng

for line in lines:
    l1 = line.split("x")
    l = int(l1[0])
    b = int(l1[1])
    h = int(l1[2])

    # ans += tsa(l, b, h)
    # ans += slack(l,b, h)
    ribb += ribbon(l,b,h)
print(ribb)