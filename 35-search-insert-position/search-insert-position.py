class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        print("target",target)
        if target in nums:
            return nums.index(target)

        for num in nums:
            print("num",num)
            if num >= target:
                print("test")
                return nums.index(num)
        return len(nums)