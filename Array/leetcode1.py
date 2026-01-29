nums = [4,1,2,1,2]
freq = {}

def singlenumber(nums):
    for i in range(0,len(nums)):
        if nums[i] in freq.keys():
            freq[nums[i]]+=1
        else:
            freq[nums[i]] = 1
    return freq



print(singlenumber(nums))