class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #mock interview questions
        res,n=0,len(s)
        stack=[]
        stack.append(-1)#will fail for cases that start with ) [)(())]
        for i in range(n):
            #print(stack,i,s[i])
            if s[i]=='(':
                stack.append(i)
            else:
                # if stack:#will fail for ()
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    #print(stack,i,s[i])
                    res=max(res,i-stack[-1])
        return res

            


        