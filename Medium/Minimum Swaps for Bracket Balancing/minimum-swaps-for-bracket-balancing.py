#User function Template for python3
class Solution:
    def minimumNumberOfSwaps(self,S):
        # code here 
        
        o, c = 0, 0
        cnt  = 0
        for i in range(len(S)):
            if S[i] == ']':
                c += 1
            else:
                if c > o:
                    #print(o,c)
                    cnt += (c-o)
                o += 1        

        return cnt
                
                
        # Minimum adjacent Swaps for Bracket Balancing
        ''''
        c=0
        o=0
        unbalanced=0
        ans=0
        
        n=len(S)
        
        for i in range(n):
            
            if S[i]==']':
                c+=1
                
                unbalanced=c-o
                
            if S[i]=='[':
                o+=1
                
                if unbalanced>0:
                    ans+=unbalanced
                    unbalanced-=1
                    
                    
        if unbalanced==0:
            return ans
            
        else :return -1
                
                
        '''    
                


        




#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        ob = Solution()
        print(ob.minimumNumberOfSwaps(S))
# } Driver Code Ends