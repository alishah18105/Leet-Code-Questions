#Write a function that reverses a string. The input string is given as an array of characters s.
s = ["h","e","l","l","o"]
i = 0
j = len(s) -1
while i<j:
    s[i], s[j] = s[j], s[i]
    i+=1
    j-=1
print(s)