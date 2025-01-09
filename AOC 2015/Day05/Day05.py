f = open("input.txt", "r")
lines = f.readlines()
ans = 0
# bol = False
add1 = 0
#
# def vowelcount(line):
#     vcount = 0
#     for i in line:
#         if i in ["a","e","i","o","u"]:
#             vcount += 1
#     if vcount > 2:
#         return True
#     else:
#         return False
#
# def double(line):
#     for j in range(len(line)-1):
#         if line[j] == line[j+1]:
#             return True
#     else:
#         return False
#
#     # for j in line:
#
#
# def conditionstr(line):
#     temp = ["ab", "cd", "pq", "xy"]
#     for k in temp:
#         if k in line:
#             return False
#     else:
#         return True
#
# for line in lines:
#     if vowelcount(line) and double(line) and conditionstr(line):
#         ans+= 1
#         # print(line)
#
# print(ans)


def sandwitch(line):
    for let in range(1, len(line)-1):
        if line[let-1] == line[let+1]:
            return True
    else:
        return False

def twicedouble(line):
    for fir in range(len(line)-3):
        for sec in range(fir+2, len(line)-1):
            if line[fir] == line[sec] and line[fir+1] == line[sec+1]:
                return True
    else:
        return False



for line in lines:
    if sandwitch(line) and twicedouble(line):
        add1 += 1

print(add1)