#User function Template for python3

class Solution:
    def longestUniqueSubsttr(self, S):
        # code here
        
        mp={}
        j=0
        ans=0
        
        for i in range(len(S)):
            
            if S[i] in mp:
                mp[S[i]]+=1
                
            else:
                mp[S[i]]=1
                
                
            while j<i and mp[S[i]]>1:
                mp[S[j]]-=1
                
                j+=1
                
            ans=max(ans, i-j+1)
            
        
        return ans
                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends