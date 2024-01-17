#User function Template for python3

class Solution:
    def permutationCoeff(self,n, k):
        # Code here
        ans=1
        mod=10**9+7
        for i in range(k):
            ans=(ans*n)%mod
            n-=1
            
        return ans%mod
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k) 
		ob = Solution();
		ans = ob.permutationCoeff(n, k)
		print(ans)
# } Driver Code Ends