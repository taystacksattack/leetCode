class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # for i in range(len(nums)):
        #     print(nums[i])
        #     for j in range(1,len(nums)):
        #         if i!=j and nums[i] + nums[j] == target:
        #             return [i,j]

        #with hash map
        hash = {}

        for i, num in enumerate(nums): #enumerate gives index and value
            complement = target-num
            if complement in hash:
                return [i, hash[complement]]
            else:
                hash[num]=i

        