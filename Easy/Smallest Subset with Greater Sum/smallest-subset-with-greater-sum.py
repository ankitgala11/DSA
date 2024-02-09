#User function Template for python3

class Solution:
    def minSubset(self, A,N):
        
        j=0
        s=0
        t=sum(A)
        A.sort()
        ans=float('inf')
        
        for i in range(N):
            s+=A[i]
            t-=A[i]
            
            while s>t:
                ans=min(ans, i-j+1)
                
                s-=A[j]
                t+=A[j]
                
                j+=1
                
                
            
        return ans
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSubset(A,N)
        print(ans)
# } Driver Code Ends