#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        # Your code goes here 
        
        ans=0
        arr.sort()
        
        i=N-2
        j=N-1
        
        
        while i>=0:
            
            if arr[j]-arr[i]<K:
                # print(arr[i], arr[j])
                ans+=arr[i]+arr[j]
                i-=2
                j-=2
                
            else:
                i-=1
                j-=1
                
                
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends