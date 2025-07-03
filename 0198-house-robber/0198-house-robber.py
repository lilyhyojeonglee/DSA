class Solution:
    def rob(self, nums: List[int]) -> int:
        #[1,2,3,1]
        #[1,2,1+3=4,(2+1<4)=4]
        n = len(nums)

        if n==1:
            return nums[0]
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[1],nums[0])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+ dp[i-2])
        
        return dp[n-1]

            