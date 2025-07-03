class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        minnum = len(nums)/2
        for i in nums:
            count[i] = count.get(i, 0) + 1
            if count[i]> minnum:
                return i

        