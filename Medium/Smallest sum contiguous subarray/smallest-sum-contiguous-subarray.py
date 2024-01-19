#User function Template for python3


class Solution:
    def smallestSumSubarray(self, arr, N):
        #Your code here
        
        currsum=arr[0]
        ans=currsum
        
        for i in range(1, N):
            currsum+=arr[i]
            
            currsum=min(currsum, arr[i])
            ans=min(ans, currsum)
            
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.smallestSumSubarray(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends