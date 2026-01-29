digits = [3,2,1]

def plusOne(digits):
    sum = 0
    for i in range(0,len(digits),1):
        sum = (sum *10) + digits[i]
    sum+=1
    return [int(d) for d in str(sum)]
print(plusOne(digits))