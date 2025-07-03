class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0],self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        prevprev, prev =0,0

        for n in nums:
            temp = max(prevprev + n, prev)
            prevprev = prev
            prev = temp
        return prev
    
        
        
        