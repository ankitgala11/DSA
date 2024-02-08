from typing import List

class Solution:

    def buyMaximumProducts(self, n: int, k: int, price: List[int]) -> int:

        ans = 0

        pair = []

        for i in range(n):

            pair.append([price[i], i+1])

        pairs = sorted(pair, key=lambda x: x[0])

        for i in range(len(pairs)):

            price = pairs[i][0]

            stock = pairs[i][1]

            if stock*price <= k:

                ans += stock

                k -= price*stock

            else:

                ans += k//price

                k =0

        return ans

# from typing import List
# class Solution:
#     def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
#         # code here
#         ans=0
#         temp=[]
#         for i in range(n):
#             temp.append([price[i], i+1])
#         temp.sort()
        
#         def bs(s, e, val, tar):
#             ans=0
#             while s<=e:
#                 m=(s+e)//2
#                 if m*val<=tar:
#                     ans=m
#                     s=m+1
                    
#                 else:
#                     e=m-1
                    
#             return ans
            
#         total_purchase = 0
#         for i in range(n):
#             P = min(temp[i][1], k//temp[i][0])
#             total_purchase += P
#             k -= (P * temp[i][0])
     
#         return total_purchase
        
 
#         # for i in range(n):
            
#         #     # for j in range(temp[i][1]):
                
#         #     t=bs(1, temp[i][1], temp[i][0], k)
#         #     ans+=t
#         #     k-=temp[i][0]*t
#         #         # if temp[i][0]<=k:
#         #         #     ans+=1
#         #         #     k-=temp[i][0]
#         #         # else:
#         #         #     break
                
#         # return ans
            
        
                
            
        






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
        
        n,k = map(int,input().strip().split())
        
        price=IntArray().Input(n)
        
        obj = Solution()
        res = obj.buyMaximumProducts(n, k, price)
        
        print(res)
        

# } Driver Code Ends