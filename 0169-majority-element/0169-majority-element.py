class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = {}
        # minnum = len(nums)/2
        # for i in nums:
        #     count[i] = count.get(i, 0) + 1
        #     if count[i]> minnum:
        #         return i

        res = nums[0]
        count = 1
        for i in nums[1:]:
            if i == res:
                count+=1
            
            elif i != res and count ==0:
                res = i
                count +=1
            else:
                count -=1
        
        return res



        