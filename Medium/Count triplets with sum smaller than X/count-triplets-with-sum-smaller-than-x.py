class Solution:
    def countTriplets(self, arr, n, sumo):
        #code here
        arr.sort()
        ans=0
        
        # print(arr)
        for i in range(n):
            
            j=i+1
            k=n-1
            
            while j<k:
                
                s=arr[i]+arr[j]+arr[k]
                
                
                # k-j because if sum of i j k < target then i j k-1, i j k-2 .... 
                # will also be less than target
                
                if s<sumo:
                    ans+=k-j
                    j+=1
                    
                else:
                    k-=1
                    
                    
                    
                
                
        return ans
                
        
        
        
        
        # for i in range(n-2):
            
        #     for j in range(i+1, n-1):
                
        #         for k in range(j+1, n):
                    
        #             if sumo>arr[i]+arr[j]+arr[k]:
        #                 ans+=1
              
                
                
        # return ans





#{ 
 # Driver Code Starts

t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    k=l[1]
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.countTriplets(a,n,k)
    print(ans)
# } Driver Code Ends