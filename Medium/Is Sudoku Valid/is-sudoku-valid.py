#User function Template for python3
import sys
sys.setrecursionlimit(10**8)


class Solution:
    def isValid(self, mat):
        # code here
        
        def check(i, j, k):
            cnt=0
            for z in range(9):
                
                if z!=j and mat[i][z]==k:
                    
                    return False
                    
                    
                if z!=i and mat[z][j]==k:
                    return False
                    
                    
                    
                if mat[3 * (i//3) + z//3][3 * (j//3) + z%3]==k:
                    cnt+=1
                    
                    if cnt>=2:
                        return False
                    
                    
            return True
            
            
            
        def solve():
            
            for i in range(9):
                for j in range(9):
                    
                    if mat[i][j]!=0:
                        
                        if check(i, j , mat[i][j])==False:
                            return 0
                        
                        # for k in range(1, 10):
                            
                            
                        #     if canPlace(i, j, k):
                                
                        #         mat[i][j]=k
                                
                        #         if solve():
                        #             return 1
                                    
                        #         else:
                        #             mat[i][j]=0
                                    
                                    
                                    
                        # return 0
                    
            return 1
        
        return solve()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends