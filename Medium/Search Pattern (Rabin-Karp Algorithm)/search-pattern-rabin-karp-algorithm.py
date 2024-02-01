#User function Template for python3

class Solution:
    def search(self, patt, s):
        
        # sliding window -----------------------------------------------------------
        # sliding technique does not work as we neet to maintain the order of alphabets in string
        
        # eg s = abca 
        #   p = abc
           
           
        #   Acc to sliding tech ans will be 1,2 as it will give true for bca but we need abc order
        #   so only ans is 1
        
            
        # KMP-----------------------------------------------------------
        n=len(patt)
        arr=[0]*n
        
        for i in range(1, n):
            j=arr[i-1]
            while j>0 and patt[i]!=patt[j]:
                j=arr[j-1]
                
            if patt[i]==patt[j]:
                j+=1
                
            arr[i]=j
            
            
        j=0
        ans=[]
        i=0
        
        m=len(s)
        
        while i<m :       
            if s[i]==patt[j]:
                i+=1
                j+=1
                
            else:
                if j!=0:
                    j=arr[j-1]
                    
                else:
                    i+=1
                
            if j==n:
                ans.append(i-j+1)
                j=arr[j-1]
                
        
                    
        if not ans:
            return [-1]
        else:
            return ans
            
            
        # Rabin karp :( -----------------------------------------------------------
        
        # n=len(s)
        # m=len(patt)
        
        # d=256
        # q=7
        
        
        # p=0
        # t=0
        # h=1
        
        # ans=[]
        
        # for i in range(m-1):
        #     h=(d*h)%q
            
        # for i in range(m):
        #     p=(p*d + ord(patt[i]) )%q
        #     t=(t*d + ord(s[i]) )%q
            
            
        # for i in range(n-m + 1):
        #     if p==t:
        #         for j in range(m):
        #             if patt[j]!=s[i+j]:
        #                 break
        #             j+=1
                    
        #         if j==m:
        #             ans.append(i+1)
                
                
        #     if i<n-m:
        #         # t = ((d * (t - v[character to be removed] * h) + v[character to be added] ) mod 13 
        #         t=( d*(t-ord(s[i])*h) + ord(s[i+m])) % q
        #         if t<0:
        #             t+=q
                    
                
        # if ans:return ans
        # else: return [-1]
        
        
        
        
        
        
        #   built in find funct -----------------------------------------------------------
        
        # i=-1
        
        # ans=[]
        # # print(s.find("patt", 2))
        
        # while s.find(patt, i+1)!=-1:
        #     ans.append( s.find(patt, i+1) +1 )
        #     i = s.find(patt, i+1)
            
        # if ans:
        #     return ans
            
        # else:
        #     return [-1]





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends