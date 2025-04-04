class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m,o=len(s1),len(s2),len(s3)
        if n+m!=o:
            return False
        # dp={}
        # def dfs(i,j,k):
        #     if k==o and i==n and j==m:
        #         return True
        #     if (i,j) in dp:
        #         return dp[(i,j)]
        #     res=False
        #     if i<n and s1[i]==s3[k]:
        #         res=dfs(i+1,j,k+1)
        #     if j<m and s2[j]==s3[k]:
        #         res=dfs(i,j+1,k+1)
            
        #     dp[(i,j)]=res
        #     return res
        # return dfs(0,0,0)

            
        # n,m,o=len(s1),len(s2),len(s3)
        # if n+m!=o:
        #     return False
        dp=[[False]*(m+1) for _ in range(n+1)]
        dp[n][m]=True
        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if i<n and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<m and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True

        return dp[0][0]

