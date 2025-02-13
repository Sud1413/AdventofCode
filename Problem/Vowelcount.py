str1 = str(input("Enter a string:- "))
vcount = 0

for i in range(len(str1)):
    if str1[i] in ["a","e","i","o","u"]:
        vcount += 1
print(vcount)