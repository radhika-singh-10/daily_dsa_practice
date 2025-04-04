class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #google question 
        l,r=1,max(piles)
        #we take max instead of last element for r because its unsorted piles
        while l<r:
            m=(l+r)//2
            hr_spent=0
            for pile in piles:
                hr_spent+=math.ceil(pile/m)
            #if koko can finish eating in h, she can finish eating in h+1
            #else she cant finsih eating h-1 
            if hr_spent<=h:
                r=m
            else:
                l=m+1
        return r

        