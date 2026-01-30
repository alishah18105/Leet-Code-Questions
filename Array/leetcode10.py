#Given an integer array nums, return true if any value appears at least twice in the array, and return false if 
# every element is distinct.
nums = [1,2,3,1]

def containsDuplicate(nums):
    newList = []
    for i in range(0, len(nums),1):
        if nums[i] in newList:
            return True
        else:
            newList.append(nums[i])
    return False
print(containsDuplicate(nums))

