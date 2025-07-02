class Solution:
    def simplifyPath(self, path: str) -> str:
        splitpath = path.split("/")
        res = []
        for s in splitpath:
            if s == "..":
                if res:
                    res.pop()
            elif s and s!=".":
                res.append(s)
        
        return "/"+ "/".join(res)