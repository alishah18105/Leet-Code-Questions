#Given a string s, reverse only all the vowels in the string and return it.4
s = "leetcode"
vowels = ("a", "e", "i", "o", "u")
char = list(s)
i=0
j= len(s) -1
while i<j:
    if char[i].lower() not in vowels:
        i+=1
    elif char[j].lower() not in vowels:
        j-=1
    else:
        char[i], char[j] = char[j], char[i]
        i+=1
        j-=1

result = "".join(char)
print(result)
