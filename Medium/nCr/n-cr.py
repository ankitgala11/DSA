#User function Template for python3

# ncr = n! / r! * (n-r)!
    
mod=10**9 + 7    

class Solution:
    def nCr(self, n, r):
        # code here
        if r > n :return 0
        
        def fact(n, end):
            
            ans=1
            while end:
                ans*=n
                n-=1
                end-=1
                
            return ans
            
            
            
        return (fact(n, r)//fact(r, r-1))%mod
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, r = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.nCr(n, r))
# } Driver Code Ends