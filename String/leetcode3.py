#Given a string s, return true if it is a palindrome, or false otherwise.
text = "0P"
result = ("". join(char for char in text if char.isalnum())).lower()
reverse = result[::-1]
if(result == reverse):
    print("True")
else:
    print("False")

