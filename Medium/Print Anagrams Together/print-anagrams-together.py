#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        
        mp={}
        
        for i in range(n):
            a=tuple(sorted(words[i]))
            if a in mp:
                mp[a].append(i)
            else:
                mp[a]=[i]
            
            
        ans=[]
        
        for i in mp:
            temp=[]
            for j in mp[i]:
                temp.append(words[j])
                
                
            ans.append(temp)
            
            
        return ans
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends