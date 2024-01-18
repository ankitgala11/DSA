#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
class Solution:
    def maxChainLen(self,Parr, n):
        # Parr:  list of pair
        #code here
        Parr.sort(key=lambda x:x.b)
        cnt=1
        temp=Parr[0].b
        
        for i in range(1, n):
            if Parr[i].a>temp:
                cnt+=1
                temp=Parr[i].b
                
                
            
        return cnt
            
            
        
        
        
        
        
        # This works but TLE
        # def solve(i, prev):
            
        #     if i>=n:
        #         return 0
                
        #     if dp[i][prev+1]!=-1:
        #         return dp[i][prev+1]
                
        #     # inc
        #     inc=0
        #     if prev==-1 or Parr[i].a>Parr[prev].b:
        #         inc=1+solve(i+1, i)
            
        #     # exc
        #     exc=solve(i+1, prev)
            
            
        #     dp[i][prev+1]= max(inc, exc)
        #     return dp[i][prev+1]
            
            
            
            
            
            
        # dp=[[-1]*n for _ in range(n)]
        # return solve(0, -1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))
        obj=Solution()
        print(obj.maxChainLen(Parr, n))
# } Driver Code Ends