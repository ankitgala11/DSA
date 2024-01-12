from typing import List


class Solution:
    def numberOfTriangles(self, n : int, g : List[List[int]]) -> int:
        # code here
        
        '''
        
        Taking 3 DIFFERENT points 
        checking in adj matrix if an edge is there between those 3 
        if yes adding cnt
        
        cnt will increase for all permutations of same triangle 
        thus we divide it 
        
        by 3 for directed as 3 permutations
        by 6 for undirected as 6 permutations
        
        
        '''
        cnt=0
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
    
                    if i!=j and j!=k and k!=i and g[i][j]==1 and g[j][k]==1 and g[k][i]==1:
                  
                        cnt+=1
                        
                    
                
            
        return cnt//3 #for directed
        #return cnt//6 #for undirected
                        
                        

#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        g=IntMatrix().Input(n, n)
        
        obj = Solution()
        res = obj.numberOfTriangles(n, g)
        
        print(res)
        

# } Driver Code Ends