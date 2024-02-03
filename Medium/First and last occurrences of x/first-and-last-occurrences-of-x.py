#User function Template for python3
import bisect

class Solution:
    def find(self, arr, n, x):
        
        # code here
        
        f=bisect.bisect_left(arr, x)
        s=bisect.bisect(arr, x)
        
        if arr[f]!=x:
            return [-1, -1]
        return [f, s-1]


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends