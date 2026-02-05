#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#Each letter in pattern maps to exactly one unique word in s.
#Each unique word in s maps to exactly one letter in pattern.
#No two letters map to the same word, and no two words map to the same letter.

pattern = "abba"
s = "dog cat cat dog"
char = s.split()
record = {}

result = True
i=0
if len(pattern) == len(char):
    while i<len(pattern):
        if pattern[i] not in record:
            record[pattern[i]] = char[i]
            i+=1
        elif record[pattern[i]] != char[i]:
            result= False
            break
        else:
            i+=1
else:
    result = False


print(record)
