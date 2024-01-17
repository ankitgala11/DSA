#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        
        # sliding window
        i=0
        j=0
        ans=0
        temp=1
        
        while i<n:
            temp*=a[i]
            
            while j<=i and temp>=k:
                temp//=a[j]
                j+=1
              
            ans+=i-j+1   
                
            i+=1
            
        return ans
            
            
        
        
        
        # Two loops O(n^2) O(1)
        # res=0
        
        # for i in range(n):
        #     ans=1
        #     for j in range(i, n):
        #         ans*=a[j]
        #         if ans<k:
        #             res+=1
                    
        #         else:
        #             break
                
                
                
        # return res
            
    
    
    
    


#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends