#User function Template for python3

 #Your task is to complete this Function \

class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        
        l_a=len(A)
        l_b=len(B)
        l_c=len(C)
        
        if l_c!=l_a+l_b:
            return 0
        
        def solve(i, j, k):
            if i>=l_c:
                return True
            
            
            if dp[j][k]!=-1:
                return dp[j][k]
            
            q=0
            r=0
                
                
            if j<len(A) and C[i]==A[j]:
                q = solve(i+1, j+1, k)
                
            if k<len(B) and C[i]==B[k]:
                r = solve(i+1, j, k+1)
          
                
                
            dp[j][k] = q or r
            return dp[j][k]
                    
                    
                
                
       
                
        dp=[[-1]*(l_b+1)  for _ in range(l_a+1)]         
        return solve(0, 0, 0)
        
        
        
        '''
        Tabular for reference
        
        
       int n=a.size();
       int m=b.size();
       bool dp[n+1][m+1];
       memset(&dp,false,sizeof(dp));
       dp[0][0]=true;
          for (int i = 0; i <=n; i++)
       {
           for (int j = 0; j <=m; j++)
           {
               if (i==0 || j==0)
               {
                   dp[i][j]=true;
               }
               
           }
       }
       for (int i = 1; i <=n; i++)
       {
           for (int j = 1; j <=m; j++)
           {
              if (a[i-1]==c[i+j-1])
              {
                  dp[i][j]|=dp[i-1][j];
              }
              if (b[j-1]==c[i+j-1])
              {
                  dp[i][j]|=dp[i][j-1];
              }
              
              
           }
           
       }
       return dp[n][m];
       
        '''
        
        
    
                
                
                    
            
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends