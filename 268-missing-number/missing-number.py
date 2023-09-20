class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        if nums[0] != 0: return 0
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i] + 1:
                return nums[i] +1 
        return len(nums)