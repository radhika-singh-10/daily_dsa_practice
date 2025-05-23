class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        l,r=2,x//2
        while l<=r:
            m=l+(r-l)//2
            pivot=m*m
            if pivot<x:
                l=m+1
            elif pivot>x:
                r=m-1
            else:
                return m
        return r

