#User function Template for python3

class Solution:
    def isKPartitionPossible(self, a, k):
        #code here
        
        # check if sum of a is proper divisible by k if not then return 0
        s=sum(a)
        if s%k!=0:
            return 0
            
        s=s//k
        
        
        n=len(a)
        vis=set()
        
        def solve(i, currsum, k):
                
            # heree k==0 should always be at top of base case as when k==0 there are chances i>=n so if that
            # case is writen ontop it will give false
            if k==0:
                return True
                
            if currsum==s:
                return solve(0, 0, k-1)
                
            if i>=n or currsum>s:
                return False


                
            for idx in range(i , n):
                if idx not in vis :
                    vis.add(idx)
                    
                    if solve(idx+1, currsum+a[idx], k):
                        return True
                        
                    vis.remove(idx)
                 
                
            return False
            
                
        # so here we need to make  s (ie tot//k )   k times if can be done return True
       
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