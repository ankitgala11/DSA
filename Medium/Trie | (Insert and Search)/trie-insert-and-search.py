#User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""
#Function to insert string into TRIE.
def insert(root,key):
    
    #code here
    r=root
    for ch in key:
            
        if r.children[ord(ch)-97]==None:
            r.children[ord(ch)-97]=TrieNode()
        r=r.children[ord(ch)-97]
            
        
    r.isEndOfWord=True
                

#Function to use TRIE data structure and search the given string.
def search(root, key):
    
    #code here

    for ch in key:
        if root.children[ord(ch)-97]==None:
            return False
        
        root=root.children[ord(ch)-97]
            
            
    return root.isEndOfWord


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root =TrieNode()
        
#use only 'a' through 'z' and lower case
def charToIndex(ch):
    return ord(ch)-ord('a')

if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=input().strip().split()
        strs=input()
        
        t=Trie()
        
        for s in arr:
            insert(t.root,s)
        
        if search(t.root,strs):
            print(1)
        else:
            print(0)
# } Driver Code Ends