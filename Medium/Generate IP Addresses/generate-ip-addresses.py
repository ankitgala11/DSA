#Your Function should return a list containing all possible IP address
#No need to worry about order
class Solution:
    def genIp(self, s):
        #Code here
        n=len(s)
        ans=[]
        
        def check(st):
            l=len(st)
            
            if l<1 and l>3:return False
            
            if l>1 and st[0]=='0' :return False
            
            if not st: return False
            st=int(st)
            if st<0 or st>255:
                return False
            
            
            
            return True
            
            
            
            
        def gen(i,j,k):
            str1=s[:i]
            str2=s[i:j]
            str3=s[j:k]
            str4=s[k:]
            
            if check(str1) and check(str2) and check(str3) and check(str4):
                return str1+"."+str2+"."+str3+"."+str4
                
            return ""
        
        for i in range(1,n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    
                    temp= gen(i,j,k)
                    if temp:
                        ans.append(temp)
        
        return ans
            
        





#{ 
 # Driver Code Starts
#Main
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        res = Solution().genIp(s)
        res.sort()
        if(len(res)):
            for u in res:
                print(u)
        else:
            print(-1)
# } Driver Code Ends