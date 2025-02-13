str1 = str(input("Enter first string:- "))
str2 = str(input("Enter second string:- "))


for i in set(str1):
    if str1.count(i) != str2.count(i):
        print("Not Anagram")
        break
else:
    print("Anagram")