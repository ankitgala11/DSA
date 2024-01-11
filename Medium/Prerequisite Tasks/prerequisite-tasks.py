#User function Template for python3
from collections import defaultdict

class Solution:
    def isPossible(self,N,P,prerequisites):
        #code here
        
        # check if it contains cycle 
        # if it does it is not possible 
        
        adj=defaultdict(list)
        
        for i in prerequisites:
            adj[i[1]].append(i[0])
            
        vis=[0]*N
        pathvis=[0]*N
        
        
        def dfs(i):
            vis[i]=1
            pathvis[i]=1
            
            for nbr in adj[i]:
                if vis[nbr]==0:
                    if dfs(nbr):return True
                    
                elif pathvis[nbr]==1:
                    return True
                    
           
            
            
            
            pathvis[i]=0
            return False
            
            
        for i in range(N):
            if vis[i]==0:
                if dfs(i):
                    return False
                    
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # # bfs
        # adj=defaultdict(list)
        # indegree=[0]*N
        
        # for i in prerequisites:
        #     adj[i[1]].append(i[0])
        #     indegree[i[0]]+=1
            
        
            
        
        
        # q=[]
        # for i in range(N):
        #     if indegree[i]==0:
        #         q.append(i)
                
                
                
        # # print(indegree)
        # cnt=0
            
        # while q:
        #     curr=q.pop(0)
        #     cnt+=1
            
        #     for nbr in adj[curr]:
        #         indegree[nbr]-=1
                
        #         if indegree[nbr]==0:
        #             q.append(nbr)
                    
                    
                
        # # print(cnt)
        # if cnt==N:
        #     return True
            
        # return False
                
                
                
        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,P,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends