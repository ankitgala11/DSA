# User function Template for Python3

class Solution:
    def eulerPath(self, N, graph):
        # code here
        cnt=0
        for i in range(N):
            if sum(graph[i])&1:
                cnt+=1
                
        
        if cnt==0 or cnt==2:
            return 1
        return 0


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        graph = []
        for i in range(N):
            graph.append(list(map(int, input().strip().split())))
        
        ob = Solution()
        print(ob.eulerPath(N, graph))
# } Driver Code Ends