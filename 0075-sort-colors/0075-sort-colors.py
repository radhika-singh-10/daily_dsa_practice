class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1,p2=0,len(nums)-1
        cur=p0=0

        while cur<=p2:
            if nums[cur]==0:
                nums[p0],nums[cur]=nums[cur],nums[p0]
                p0+=1
                cur+=1
            elif nums[cur]==2:
                nums[cur],nums[p2]=nums[p2],nums[cur]
                p2-=1
            else:
                cur+=1
