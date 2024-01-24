#User function Template for python3

class Solution:
    def findPosition(self, N):
        # code here 

        cnt=0
        ans=0
        while N:
            if N&1:
                cnt+=1
            ans+=1
                
                
            N>>=1
            
        
        if cnt==0 or cnt>1:
            return -1
            
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        
        ob = Solution()
        print(ob.findPosition(N))
# } Driver Code Ends