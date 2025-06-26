class Solution:
    def reverse(self, x: int) -> int:

        a = abs(x)
        
        
         
        a = str(a)[::-1]
        if x<0:
            a = -int(a)
        else:
            a = int(a) 
        if a<=-pow(2,31) or a >= pow(2,31) -1:
            return 0
        return a
        