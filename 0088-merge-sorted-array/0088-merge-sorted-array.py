class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for i in range(n):
        #     nums1[m+i] = nums2[i]
        
        # nums1.sort()
        # return nums1
        x =m-1
        y = n-1
        z =m+n-1
        if n==0: return
        while z>=0 and y>=0:
            if x>=0 and nums1[x] > nums2[y]:
                nums1[z] = nums1[x]
                x-=1
            else:
                nums1[z] = nums2[y]
                y-=1
            z-=1
        
