#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        l,m=0,0
        h=n-1
        
        while(m<=h):
            if arr[m]==0:
                arr[m], arr[l] = arr[l], arr[m]
                l+=1
                m+=1
                
            elif arr[m]==1:
                m+=1
                
            else:
                arr[m], arr[h] = arr[h], arr[m]
                h-=1
                
        return arr
                
        
    









#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends