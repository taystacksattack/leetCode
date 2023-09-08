class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ''' 
        track two pointers
        
        have while lp is < len(num)
            if lp == rp:
                remove the element (nums[rp].pop())
                don't need to change rp index in this case because we removed the value, so we just continue
            Otherwise, rp can move over, then it starts over again
            if rp = len(num)-1:
                then lp moves over one, and rp becomes lp + 1

        then you can just return the length

        '''


        # This works well if the array is not sorted!!!!
        # lp = 0
        # rp = 1

        # while lp < len(nums) - 1:
        #     if nums[lp] == nums[rp]:
        #         nums.pop(rp)
        #         continue
        #     if rp == len(nums)-1:
        #         lp += 1
        #         rp = lp + 1
        #     else: rp += 1
        
        # return len(nums)


        # this is BETTER

        # replace = 1
        # for i in range(len(nums)):
        #     # print("i",i)
        #     # print("replace",replace)
        #     if nums[i] == nums[i+1]:
        #         popped = nums.pop(replace)
        #         print("popped",popped)
        #         print("nums",nums)
        #         print('length', len(nums))
        #         continue
        #     replace += 1
        
        # # return print("here's nums",nums)
        # return len(nums)


        if not nums:
            return 0

        replace = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[replace] = nums[i]
                replace += 1
        
        return replace
            