class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p_merge = m + n - 1  # Pointer for merged array
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p_merge] = nums1[p1]
                p1 -= 1
            else:
                nums1[p_merge] = nums2[p2]
                p2 -= 1
            p_merge -= 1
            
        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p_merge] = nums2[p2]
            p2 -= 1
            p_merge -= 1


        """
        Do not return anything, modify nums1 in-place instead.
        // make new set
        //loop through first array, adding elements to the set
        // loop through second, if the element is not in the set, then push element into the first array
        //sort the array. call it a day. 
        """