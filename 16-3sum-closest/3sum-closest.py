class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        '''
        sort the array
        absoluteDiff
        absoluteSum
        loop through:
        for i in range(len(nums)):
            left pointer, right pointer

            while (left < right):
                currentSum = nums[i] + nums[left]+ nums[right]
                currentDiff = absolute value of currentSum - target
                
                if currentDiff < absoluteDiff:
                    absoluteDiff = currentDiff
                    absoluteSum = currentSum

                if currentSum == target: return currentSum

                elif currentSum < target:
                    left += 1

                else:
                    right -= 1

        return absoluteSum

        '''
        nums.sort()
        absoluteDiff = 200001
        absoluteSum = 0

        for i in range(len(nums)):
            left = i+1
            right = len(nums) -1
            # print("left right", left, right)
            while (left < right):
                currentSum = nums[i] + nums[left] + nums[right]
                # print("currentsum" , currentSum)
                currentDiff = abs(currentSum - target)

                if currentDiff < absoluteDiff: 
                    absoluteDiff = currentDiff
                    absoluteSum = currentSum

                if currentSum == target: return currentSum

                elif currentSum < target:
                    left += 1
                else: right -= 1
        
        # print(absoluteDiff)
        return absoluteSum


