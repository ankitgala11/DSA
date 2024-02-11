from collections import defaultdict

class Solution:
    def pathMoreThanK (self, V, E, K, A):
        # code here
        adj=defaultdict(list)
        
        for i in range(0, len(A), 3):
            adj[A[i]].append((A[i+1], A[i+2]))
            adj[A[i+1]].append((A[i], A[i+2]))
            
            
        def dfs(i, wt):
            
            
            if wt>=K:
                return True
            vis.add(i)

            for nbr, w in adj[i]:
                
                if nbr not in vis:
                    
                   
                    
                    if dfs(nbr, wt+w):
                        return True
                        
                    vis.remove(nbr)
                        
                        
            
            
            
            
            
        wt=0
        vis=set()
        
        if dfs(0, wt):
            return 1

        return 0




#{ 
 # Driver Code Starts



if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        V, E, K= map(int, input().split())
        A = list(map(int, input().split()))
        ans = ob.pathMoreThanK(V, E, K, A);
        if(ans):
            print(1)
        else:
            print(0)


# } Driver Code Ends