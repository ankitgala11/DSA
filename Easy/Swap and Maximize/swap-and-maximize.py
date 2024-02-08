#User function Template for python3


def maxSum(arr,n):
    # code here
        arr.sort()
        ans=0
        i=0
        j=n-1
        f=0
        
        while i<j:
        
            temp=abs(arr[j]-arr[i])
            ans+=temp
            
            if f:
                j-=1
                
                
            else:
                i+=1
                
            f= not f
            
            
            # 162534
        ans+=abs(arr[i]-arr[0])
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    arr = list(map(int,input().split()))
    ans=maxSum(arr,n)
    print(ans)

# } Driver Code Ends