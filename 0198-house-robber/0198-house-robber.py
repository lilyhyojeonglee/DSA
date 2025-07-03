class Solution:
    def rob(self, nums: List[int]) -> int:
        #[1,2,3,1]
        #[1,2,1+3=4,(2+1<4)=4]
        prevprev, prev = 0,0
        for i in nums:
            temp = max(prevprev+i, prev)
            prevprev = prev
            prev = temp
        return temp
            