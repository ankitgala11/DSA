#User function Template for python3


class Solution:
    def chooseandswap (self, A):
        # code here
        
        temp=[-1]*26
        n=len(A)
        
        for i in range(n):
            if temp[ord(A[i])-ord('a')]==-1:
                temp[ord(A[i])-ord('a')]=i
                
                
                
        
                
        # print(temp)
        
        swap=0
        
        for i in range(n):
            
            for j in range(0, ord(A[i])-ord('a')+1):
                # print(temp[j], j, i)
                if temp[j]>i:
                    swap=1
                    p=A[temp[j]]
                    q=A[i]
                    # print(A[i], A[temp[j]])
                    break
            if swap:
                break
            
                    
            
            
            
        if swap:
            ans=""
            for i in range(n):
                if A[i]==p:
                    ans+=q
                elif A[i]==q:
                    ans+=p
                else:
                    ans+=A[i]
                    
            return ans
                
            
        else:
            return A
            # if s==0:
            #     for j in range(i+1, n):
                    
            
        # m=sorted(list(set(A)))
        # mini=m.pop(0)
        
        # last=None
        # n=len(A)
        # ans=""
        # for i in range(n):
        #     if A[i]==last:
        #         ans+=A[i]
                
        #     else:
        #         if A[i]>mini:
        #             if m:
        #                 mini=m.pop(0)
        #             else:
        #                 j=i+1
        #                 while j<n:
        #                     ans+=A[j]
        #                     j+=1
        #                 break
                    
        #             if A[i]>mini:
        #                 temp=A[i]
        #                 for j in range(i, n):
        #                     if A[j]==temp:
        #                         ans+=mini
        #                         # A[j]=mini
                                
        #                     elif A[j]==mini:
        #                         ans+=temp
        #                         # A[j]==temp
        #                     else:
        #                         ans+=A[j]
                            
                        
        #                 break
        #             else:
        #                 ans+=A[i]
        #         else:
        #             ans+=A[i]
                
                
        #         last=A[i]
                
                
                
                    
            
        
        # return ans







#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        A = input()
        ans = ob.chooseandswap(A)
        print(ans)


# } Driver Code Ends