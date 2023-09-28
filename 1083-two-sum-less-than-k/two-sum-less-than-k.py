class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_val = 0
        nums = sorted(nums)
    
        left_pointer = 0
        right_pointer = len(nums) - 1

        print(nums)

        while left_pointer < right_pointer:
            print("left pointer",nums[left_pointer])
            print("right pointer",nums[right_pointer])
            if nums[left_pointer] + nums[right_pointer] < k :
                if nums[left_pointer] + nums[right_pointer] > max_val: 
                    max_val = nums[left_pointer] + nums[right_pointer]
                    print("here is the max_val", max_val)

            if left_pointer == right_pointer - 1:
                left_pointer = 0
                right_pointer -= 1
            else: left_pointer +=1
            # right_pointer-=1

        
        if max_val == 0: return -1
        return max_val