#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6]
target = 7

def searchInsert(nums, target) -> int:
   
   for i in range(0, len(nums),1):
        if nums[i] == target or nums[i] > target:
            return i
        else:
            return len(nums)
        