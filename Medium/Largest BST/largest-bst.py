#User function Template for python3

maxi=float('inf')
mini=float('-inf')

# [bst, size, max, min]

class Solution:
    # Return the size of the largest sub-tree which is also a BST
    def largestBst(self, root):
        #code here
        
        def solve(root):
            
            if not root:
                return [1,0, mini, maxi]
                
            if not root.left and not root.right:
                return [1,1, root.data, root.data]
                
                
            l=solve(root.left)
            r=solve(root.right)
            
            
            
            if l[0] and r[0]:
                
                # agar mera root left ke maxi se bada and right ke mini se chota hai toh
                if l[2]<root.data and r[3]>root.data:
                    
                    # abhi bhi bst hai, total ele kitne hue, aab mera maxi konsa hai in general r[2] hoga as
                    # root<r[2] but when r hi null hoga tab sirf r[2] return karoge toh voh 0 de dega
                    # hence max(root, r2) , similarly mini from l3 and root
                    
                    return [1,  1+l[1]+ r[1]   ,   max(root.data , r[2]) , min(root.data, l[3] ) ]
            
            # agar nahi bann raha bst toh bas fir max jitna bhi tak bana voh upar bhejte jao coz 
            # bst niche se banta hai toh biche mein break ho gaya toh wapas kabhi nahi bann sakta
            return [0, max(l[1], r[1]), 0 , 0]
            
            
            
        
        
        return solve(root)[1]





#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(1000000)

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root



if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()

        root = buildTree(s)
        ob = Solution()
        print(ob.largestBst(root))

# } Driver Code Ends