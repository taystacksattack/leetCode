class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums2_length = 0
        # while nums2_length <= len(nums2)-1:
        for i in range (len(nums1)-1, -1, -1):
            if nums2_length == len(nums2): break
            print("nums1", nums1[i])
            if nums1[i] == 0:
                nums1[i] = nums2[nums2_length]
                nums2_length += 1
            # print("nums1 after removal",nums1)

        nums1.sort()

        """
        Do not return anything, modify nums1 in-place instead.
        // make new set
        //loop through first array, adding elements to the set
        // loop through second, if the element is not in the set, then push element into the first array
        //sort the array. call it a day. 
        """