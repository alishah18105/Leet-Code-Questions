#Given a string s consisting of words and spaces, return the length of the last word in the string.
s = "   fly me   to   the moon  "
words = s.split()
print(len(words[-1]))
