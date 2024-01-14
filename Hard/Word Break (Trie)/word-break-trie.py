class TrieNode: 
    
    def __init__(self): 
        self.child={} 
        self.isEnd=False 
        
class Solution: 
    def wordBreak(self, A, B): 
        # Complete this function 
        
        
        def ins(root, word): 
            
            for ch in word: 
                if ch not in root.child: 
                    root.child[ch]=TrieNode()
                    
                root=root.child[ch] 
                
            root.isEnd=True 
                    
                    
        root=TrieNode() 
                    
        for word in B: 
            ins(root, word)
            
            
            
        def search(root, word):
            if not word:
                return True
            for ch in word:
                if ch not in root.child:
                    return False
                    
                root=root.child[ch]
                
            return root.isEnd
            
        def wordbreak(root, a):
            n=len(a)
            if n==0:return True
            
            for i in range(1, n+1):
                if search(root, a[:i]) and wordbreak(root, a[i:]):
                    return True
                    
                    
            return False
        
        
        
        
        
        return wordbreak(root, A)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		ob=Solution()
		res = ob.wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends