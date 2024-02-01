#User function Template for python3

import heapq

class Solution :
    def rearrangeString(self, str):
        #code here
        mp={}
        for i in str:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
                
                
        maxheap=[]
        
        for i, v in mp.items():
            heapq.heappush(maxheap, (-v, i ))
            
        s=""
        
        while len(maxheap)>1:
            freq1, ele1=heapq.heappop(maxheap)
            freq2, ele2=heapq.heappop(maxheap)
            
            freq1+=1
            freq2+=1
            
            s+=ele1
            s+=ele2
            
            if freq1!=0:
                heapq.heappush(maxheap, (freq1, ele1 ))
            
            if freq2!=0:
                heapq.heappush(maxheap, (freq2, ele2 ))
        
                
        if not maxheap:return s
        
        freq, ele=heapq.heappop(maxheap)
        s+=ele
        
        return s
        # main is handling the op
            
            
                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        solObj = Solution()
        str2 = solObj.rearrangeString(str1)
        if str2=='-1':
            print(0)
        elif sorted(str1)!=sorted(str2):
            print(0)
        else:
            for i in range(len(str2)-1):
                if str2[i]==str2[i+1]:
                    print(0)
                    break
            else:
                print(1)
        
# } Driver Code Ends