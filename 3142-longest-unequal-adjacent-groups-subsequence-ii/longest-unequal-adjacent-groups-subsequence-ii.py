class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        

        # adjacent indices in the subsequence, their corresponding groups are unequal
        # first condition 

        # words[ij] and words[ij+1] are equal in length
        # second condition

        #  hamming distance between them is 1,
        #  third condition and then append


        # Hamming defnination
        # def ham(word1,word2):
        #     count=0
        #     n=len(word1)
        #     for i in range(n):
        #         if word1[i]!=word2[i]:
        #             count+=1
        #     return count

        # result=[]
        # n=len(words)
        # for i in range(n):
        #     res=[words[i]]
        #     prev=groups[i]
        #     for j in range(i,n):
        #         if prev!=groups[j]:#first condition
        #             if len(res[-1])==len(words[j]):#second condition
        #                 if ham(res[-1],words[j])==1:#third condition
        #                     res.append(words[j])
        #                     prev=groups[j]
        #     print(res)
        #     if len(res)>len(result):
        #         result=res.copy()
        # return result
        def hamming(word1, word2):
            return sum(c1 != c2 for c1, c2 in zip(word1, word2))
        
        n = len(words)
        dp = [[word] for word in words]  # dp[i] stores best sequence ending at i
        
        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and len(words[j]) == len(words[i]) and hamming(words[j], words[i]) == 1:
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [words[i]]
        
        # return the longest sequence
        return max(dp, key=len)
