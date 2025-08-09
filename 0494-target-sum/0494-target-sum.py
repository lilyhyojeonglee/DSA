class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(index, total):
            # when stop? when reacheed last index
            if index == len(nums):
                return total == target
            
            # Check if in dp
            if (index,total) in dp:
                return dp[(index,total)]
            
            # if not add to dp
            dp[(index,total)] = backtrack(index+1, total + nums[index])+backtrack(index+1, total - nums[index])
            
            return dp[(index,total)]
        return backtrack(0,0)