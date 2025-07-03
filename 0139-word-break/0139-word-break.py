class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                
                lenw = len(w)
                if i+ lenw <=len(s):
                    if s[i: i+lenw] == w:
                        dp[i] = dp[i+lenw]
                if dp[i]:
                    break
        return dp[0]
                    


        