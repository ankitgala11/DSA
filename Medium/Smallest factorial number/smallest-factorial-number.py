#User function Template for python3

class Solution:
    def findNum(self, n : int):
        # Complete this function
        
        s=0
        e=n*5
        ans=-1
        
        ''''
        number of 0 will be given by number of 5 in them
        
        A simple way is to calculate floor(n/5). For example, 7! has one 5, 10! has two 5s. 
        But, numbers like 25, 125, etc have more than 5 instead of floor (n / 5). 
        For example, if we consider 28! we get one extra 5 and the number of 0s becomes 6. 
        Handling this is simple, first, divide n by 5 and remove all single 5s, 
        then divide by 25 to remove extra 5s, and so on.


Trailing 0s in n! = Count of 5s in prime factors of n! = floor(n/5) + floor(n/25) + floor(n/125) + ….
        '''
        def cntzero(m):
            
            den=5
            ans=0
            
            while m>=den:
                ans+=m//den
                den*=5
                
            return ans
                
            
        
        
        
        while s<=e:
            
            m=s+(e-s)//2
            cnt=cntzero(m)
            if cnt>=n:
                ans=m
                e=m-1
                
            else:
                s=m+1
                
                
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # tle
        # def fact(n):
        #     ans=120
        #     for i in range(6, n+1):
        #         ans*=i
                
        #     return ans
            
        # def count(f):
        #     cnt=0
        #     while f%10==0:
        #         cnt+=1
        #         f//=10
                
        #     return cnt
                
            
            
            
            
            
        i=5
        
        while i:
            f=fact(i)
            
            cnt=count(f)
            
            if cnt==n:
                return i
            i+=1
            
            





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.findNum(n))
# } Driver Code Ends