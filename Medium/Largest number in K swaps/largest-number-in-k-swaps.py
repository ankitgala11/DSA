#User function Template for python3

class Solution:
    
    #Function to find the largest number after k swaps.
    def findMaximumNum(self,s,k):
        #code here
        l=list(s)
        maxi=[int(s)]
        n=len(l)
        def swap(x,y,var):
            xx=int(l[x]);yy=int(l[y])
            xval=(10**(n-1-x))
            yval=(10**(n-1-y))
            var-=(xval*xx+yval*yy)
            var+=(xval*yy+yval*xx)
            return var
            
            
        def solve(i,k,curr):
            
            maxi[0]=max(maxi[0],curr)
            if k==0 or i==n:
                return
            
            curr_max=i
            for j in range(i,n):
                if l[j]>l[curr_max]:
                    curr_max=j
            
            if curr_max==i:
                solve(i+1,k,curr)
                    
            for j in range(i,n):
                if l[j]==l[curr_max]:
                    curr=swap(i,j,curr)
                    l[j],l[i]=l[i],l[j]
                    solve(i+1,k-1,curr)
                    curr=swap(i,j,curr)
                    l[j],l[i]=l[i],l[j]
                    
        solve(0,k,int(s))
        return maxi[0]
        # n=len(s)
        
        # def swap(i , j, temp):
        #     # print(i, j)
        #     temp= temp[0:i]+temp[j]+temp[i+1: j]+temp[i]+temp[j+1:]
        #     return temp
            
        
        # def solve(idx, k,s):
        #     nonlocal maxi
            
        #     if idx==n or k==0:
        #         if int(maxi)<int(s):
        #                 maxi=s
                
        #         return 
                
        #     # no swap
        #     solve(idx+1, k, s)
            
        #     # swap
        #     for i in range(idx+1, n):
                
        #         if s[i]>s[idx]:
        #             s=swap(idx, i, s)
                    
        #             solve(idx+1, k-1, s)
        #             s=swap(idx, i, s)
                
                    
                        
                    
            
                        


        # maxi="0"
        # solve(0,k,s )
        # return maxi



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        k = int(input())
        s = input()
        ob=Solution()
        print(ob.findMaximumNum(s,k))

# } Driver Code Ends