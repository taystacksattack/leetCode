class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2 
            #mid = left + (right-left) // 2
            #using (right-left) means it uses integer division - avoids integer overflow rather than (right - left) //2

            if nums[mid] == target:
                return mid
            elif  nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


# here it is recursively:
'''
class Solution: 
    def search(self, nums: List[int], target: int) -> int:
        def recurse (left right):
            if left >= right:
                return right if unms[right] == target else -1
            pivot = left + (right -left)//2

            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                return recurse (left, pivot -1)
            else:
                return recurse(pivot +1, right)
        
        return recurse(0, len(nums)-1)
'''