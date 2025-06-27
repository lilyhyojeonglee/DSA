class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = "" #edge case if nothing is the saem ["a", "b"]
        for i in range(len(strs[0])):
            for s in strs:
                #rejection cases? when ith indices dont align or when other strings aar shorter
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res