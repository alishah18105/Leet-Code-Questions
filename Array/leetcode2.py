#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#Increment the large integer by one and return the resulting array of digits.
digits = [3,2,1]

def plusOne(digits):
    sum = 0
    for i in range(0,len(digits),1):
        sum = (sum *10) + digits[i]
    sum+=1
    return [int(d) for d in str(sum)]
print(plusOne(digits))