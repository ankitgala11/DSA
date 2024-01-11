#User function Template for python3
from collections import defaultdict

class Solution:
    def findOrder(self,alien_dict, N, K):
    # code here
        '''
        when dict is not possible ?
        
        when larger string is before shorter  ABCD
                                              ABC 
                                              
        
        when cyclic dependency
        
        abc
        bat
        act
        
        '''
    
        # make adj list using given list and topo sort in that to give ans
    
        def topo(i):
            vis.add(i)
            
            for nbr in adj[i]:
                if nbr not in vis:
                    topo(nbr)
                    
                    
            stack.append(chr(i+97))
        
        adj=defaultdict(list)
        
        
        for i in range(N-1):
            s1=alien_dict[i]
            s2=alien_dict[i+1]
            
            n=min(len(s1) , len(s2))
            
            for j in range(n):
                if s1[j]!=s2[j]:
                    adj[ord(s1[j])-ord('a')].append(ord(s2[j] ) -ord('a'))
                    break
                
        
        vis=set()
        stack=[]
        
        for i in range(K):
            if i not in vis:
                topo(i)
        
        return stack[::-1]
                    
                    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends