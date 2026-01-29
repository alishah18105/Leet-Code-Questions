#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
#Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
#The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

nums =  [1,1,2]
def removeDuplicates(nums) -> int:
        
        for i in range (len(nums)-1, 0,-1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
        print(nums)
        return len(nums)

print(removeDuplicates(nums))