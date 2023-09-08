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

        lp = 0
        rp = 1

        while lp < len(nums) - 1:
            if nums[lp] == nums[rp]:
                nums.pop(rp)
                continue
            if rp == len(nums)-1:
                lp += 1
                rp = lp + 1
            else: rp += 1
        
        return len(nums)