#User function Template for python3

class Solution:
    def minimumDays(self, S, N, M):
        # code here
        sun=S//7
        totfoodreq=S*M
        buydays=S-sun
        foodyoucanbuy=buydays*N
        
        
        if totfoodreq>foodyoucanbuy:return -1
        
        else:
            if totfoodreq%N==0:
                return totfoodreq//N
            else:
                return (totfoodreq//N)+1
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.minimumDays(S, N, M))
# } Driver Code Ends