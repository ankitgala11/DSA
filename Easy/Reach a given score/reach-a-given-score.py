#User function Template for python3

def count(n):
    #your code here
    arr=[3, 5, 10]
    
    l=3
    
    
    def solve(i, n):
        if i>=l or n<0:
            return 0
            
        if n==0:
            return 1
            
        
        inc=solve(i, n-arr[i])
        exc=solve(i+1, n)
        
        return inc + exc
        
        
        
    return solve(0, n)
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))
        
# } Driver Code Ends