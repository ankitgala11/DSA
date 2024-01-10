#User function template for Python

class Solution:
	def shortest_distance(self, matrix):
		#Code here
		
# 		by dijkstra algo 
# 		compute min dist with each vertex as soruce 
        # O(n(e + logV))
		
# 		n**3 time complextity

		
		n=len(matrix)

        for i in range(n):
            for j in range(n):
                if matrix[i][j]==-1:
                    matrix[i][j]=10e7

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    
                    matrix[i][j]=min(matrix[i][j], matrix[i][via]+matrix[via][j] )
                        
                    
        for i in range(n):
            for j in range(n):
                if matrix[i][j]==10e7:
                    matrix[i][j]=-1
                    
                    
        # how to find if it contains neg cycle?
        # if in matrix if mat[i][i] i.e. diagonal ele goes <0 it contains neg cycle
            
        

#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends