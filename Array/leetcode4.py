#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

strs = ["dog","racecar","car"]
prefix = strs[0]

for i in range(1, len(strs)):
    while prefix != '':
        if strs[i].startswith(prefix):
            break
        else:
            prefix= prefix[:-1]
print(prefix)