#User function Template for python3

class Solution:

    def longestPalinSubseq(self, S):
        # code here
        
        # lcs of s and reverse of s
        
        def solveOpt():
            curr=[0]*(y+1) 
            next=[0]*(y+1) 
            
            for i in range(x-1, -1, -1):
                for j in range(y-1, -1, -1):
                    
                    if s1[i]==s2[j]:
                        curr[j]= 1+next[j+1]
                        
                    else:
                        curr[j]= max( curr[j+1] , next[j] )
                        
                    
                next=curr[:]
            
            return curr[0]
            
            
        s1=S
        s2=S[::-1]
        x=len(S)
        y=x
        
        return solveOpt()
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
# } Driver Code Ends