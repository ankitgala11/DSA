#User function Template for python3


class Solution:
    def maximumSumRectangle(self,R,C,M):
        #code here
        
        
        maxans=float('-inf')
        
        for i in range(R):
            temp=[0]*C
            for j in range(i, R):
                
                
                for k in range(C):
                    temp[k]+=M[j][k]
                    
                
                
                maxi=0
                for i in temp:
                    maxi+=i
                    maxi=max(maxi, i)
                    maxans=max(maxans, maxi)
            
        
        return maxans
                    
                    
                    
                    
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__=='__main__':
    t=int(sys.stdin.readline().strip())
    for _ in range(t):
        N,M=map(int,sys.stdin.readline().strip().split())
        a=[]
        for i in range(N):
            s=list(map(int,sys.stdin.readline().strip().split()))
            a.append(s)
        ob=Solution()
        print(ob.maximumSumRectangle(N,M,a))
# } Driver Code Ends