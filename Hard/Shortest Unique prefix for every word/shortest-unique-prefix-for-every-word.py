


class TrieNode():
    
    def __init__(self):
        self.child={}
        self.isEnd=False
        self.freq=0
        
        
class Solution:
    def findPrefixes(self, arr, N):
        # code here 
        root=TrieNode()
        
        def ins(root, key):
            
            curr=root
            for ch in key:
                if ch not in curr.child:
                    curr.child[ch]=TrieNode()
                    
                curr.freq+=1
                curr=curr.child[ch]
                
            curr.isEnd=True
            
        
        for i in arr:
            ins(root, i)
            
        
            
        def dfs(root, word):
            
            op="" 
            
            for ch in word:
                
                if root.isEnd or root.freq==1:
                    break
                op+=ch
                root=root.child[ch]
                
            ans.append(op)
                
        
        ans=[]
        for i in arr:
            dfs(root, i)
            
            
        return ans
            
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(str,input().split()))
        
        ob = Solution()
        res = ob.findPrefixes(arr,N)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends