class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print(self)
        # print(nums)
        # print(target)
        for i in range(len(nums)):
            print(nums[i])
            for j in range(1,len(nums)):
                if i!=j and nums[i] + nums[j] == target:
                    # return [nums.index(num1),nums.index(num2)]
                    return [i,j]