#User function Template for python3
class Solution:
    def minJumps(self, arr, n):
        #code here/
        
        if arr[0]==0:
            return -1
            
        if n==1:
            return 0
            
        steps=arr[0]
        maxreach=arr[0]
        jumps=1
        
        for i in range(1 , n):
            
            if i==n-1:
                return jumps
                
            
                
            maxreach=max(maxreach, i+arr[i])
            steps-=1
            
            if not steps:
                jumps+=1
                steps=maxreach-i
                if not steps:
                    return -1
            
            
        return jumps
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends