#User function Template for python3

class Solution:
    def palindromicPartition(self, string):
        # code here
        
        def check(s):
            return s==s[::-1]
        
        def solve(i):
            
            if i>=n:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
           
            mini=float('inf')
            op=""
            for idx in range(i, n):
                op+=string[idx]
                
                if check(op) :
                    ans=1+solve(idx+1)
                    
                    mini=min(mini, ans)
                    
                    
                
            dp[i]= mini
            return dp[i]
            
                    
                
                
          
                
                    

        n=len(string)
        
        dp=[-1]*n 
        
        return solve(0)-1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends