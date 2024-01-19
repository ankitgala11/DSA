#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        
        
        s=sum(a)
        if s%k!=0:
            return 0
            
        s=s//k
        
        
        n=len(a)
        vis=set()
        
        def solve(i, currsum, k):
            # if i>=n or currsum>s:
            #     return False
                
            if k==0:
                return True
                
            if currsum==s:
                return solve(0, 0, k-1)
                
            if i>=n:
                return False
            
                
            if currsum>s:
                return  False

                
            for idx in range(i, n):
                if idx not in vis :
                    vis.add(idx)
                    
                    if solve(idx+1, currsum+a[idx], k):
                        return True
                        
                    vis.remove(idx)
                 
                
            return False
            
                
           
                
        if solve(0, 0, k):
            return True
            
        return False
        
        
                
                
                
                





#{ 
 # Driver Code Starts


if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        N=int(input())
        arr=[int(x) for x in input().split()]
        k=int(input())
        if Solution().isKPartitionPossible(arr, k):
            print(1)
        else:
            print(0)
# } Driver Code Ends