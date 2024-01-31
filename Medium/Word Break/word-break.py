#User function Template for python3

def wordBreak(line, dictionary):
    # Complete this function
    
    def solve(word):
        if len(word)==0:return True
        
        for i in range(1, len(word)+1):
            
            if word[0:i] in d and solve( word[i:] ):
                return True
                
                
        return False
        
        
    
    d = set(dictionary)
    
    
    return solve(line)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends