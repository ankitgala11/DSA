#User function Template for python3
INT_MIN=float('-inf')
INT_MAX=float('inf')


class Solution:

    def MedianOfArrays(self, array1, array2):
            #code here
            
        # keep array1 smaller so bs is applyied on smaller array
        if len(array1) > len(array2):
            array1, array2 = array2, array1
            
        n1=len(array1)
        n2=len(array2)
  
            
        s=0
        e=n1
        total=n1+n2
        left=(n1+n2+1)//2       #doing +1 to make it work with odd even
    
        
        # left matlab kitne ele honge upto median
        
        while s<=e:
            
            m1=(s+e)//2
            # m1 is cut 1 where we take that much from array 1
            # remaining to be taken from array 2
            
            m2=left-m1
            
            l1,l2=INT_MIN,INT_MIN
            r1,r2=INT_MAX,INT_MAX
            
            
            if m1-1 >= 0 : l1=array1[m1-1]
            
            if m2-1 >= 0:l2=array2[m2-1]
            
            if m1<n1 : r1=array1[m1]
            if m2<n2 : r2=array2[m2]
            
            
            if l1<=r2 and l2<=r1:
                if total &1:    #odd
                    return max(l1, l2)
                else:
                    ans=(max(l1,l2)+min(r1,r2))/2
                    if int(ans)<ans:
                        return ans
                    else:
                        return int(ans)
                    
                    
            elif l1>r2:
                e=m1-1
                
            elif l2>r1:
                s=m1+1
                    
                
        return 0
                        
                





#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends