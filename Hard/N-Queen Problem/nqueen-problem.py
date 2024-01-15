#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        
        # O(n!) O(n2)

        board=[[0]*n for _ in range(n)]
        
        def issafe(row, col):
            if row in r and r[row]==1 or row+col in dodia and dodia[row+col]==1 or n-1+col-row in updia and updia[n-1+col-row]==1:
                return False
            return True
        
        r={}
        updia={}
        dodia={}
        
        
        ans=[]
        
        def solve(col):
            if col>=n:
                temp=[]
                for i in board:
                    for j in range(n):
                        if i[j]!=0:
                            temp.append(j+1)
                        
                ans.append(temp)
                return
            
            
            for row in range(n):
                if issafe(row, col):
                    
                    board[row][col]=1
                    
                    r[row]=1
                    updia[(n-1)+(col-row)]=1
                    dodia[row+col]=1
                    
                    solve(col+1)
                    
                    board[row][col]=0
                    
                    r[row]=0
                    updia[(n-1)+(col-row)]=0
                    dodia[row+col]=0
                    
                
                
                    
        solve(0)
        return sorted(ans)
                    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends