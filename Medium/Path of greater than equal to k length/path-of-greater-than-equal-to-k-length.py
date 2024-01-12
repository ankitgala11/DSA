from collections import defaultdict

class Solution:
    def pathMoreThanK (self, V, E, K, A):
        # code here
        adj=defaultdict(list)
        
        for i in range(0, len(A), 3):
            adj[A[i]].append((A[i+1], A[i+2]))
            adj[A[i+1]].append((A[i], A[i+2]))
            
            
        def dfs(i, wt):
            
                
            vis.add(i)

            for nbr in adj[i]:
                
                if nbr[0] not in vis:
                    
                    wt+=nbr[1]
                    
                    if wt>=K:
                        return True
                        
                    vis.add(nbr[0])
                    
                    if dfs(nbr[0], wt):
                        return True
                        
                    vis.remove(nbr[0])
                    wt-=nbr[1]
                        
                        
            
            
            
            
            
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