

from typing import List
import bisect

class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
        
class Solution:
    def findLeastGreater(self, n : int, arr : List[int]) -> List[int]:
        # code here
        
        
        
        # using bst O(nlogn) O(n^2 worst case ie )
        def solve(root, val):
            
            nonlocal suc
            
            if not root:
                root=Node(val)
                return root
                
                
            if root.data>val:
                suc=root
                root.left=solve(root.left, val)
                
            else:
                root.right=solve(root.right, val)
                
                
            return root
        
        root=None
        for i in range(n-1, -1, -1):
            suc=None
            root=solve(root, arr[i])
            
            if suc:
                arr[i]=suc.data
                
            else:
                arr[i]=-1
                
        return arr
        
        '''
        # using set
        
        # works in c++ as we dont have ordered set in python so we need to sort every time whcih gives
        # tle
        
        # intuition is add ele from behind check bisect idx if is equal to len means its biggest than all and
        # hence add -1 else add the pos
        
        # gives O(nlogn) if we can use order set
        
        # s=[arr[-1]]
        # ans=[-1]
        
        # for i in range(n-2, -1, -1):
            
        #     idx=bisect.bisect(s, arr[i])
        #     if idx==len(s):
        #         ans.append(-1)
        #     else:
        #         ans.append(s[idx])
                
        #     s.append(arr[i])
        #     s.sort()
                
                
        # return ans[::-1]

        '''

#{ 
 # Driver Code Starts


class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.findLeastGreater(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends