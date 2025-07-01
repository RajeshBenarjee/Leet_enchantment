class Solution:
    def possibleStringCount(self, word: str) -> int:
        #  a group of consicutive characters might be the error 
        # freq =1 if no possible errors and if the s[i]=s[i+1] unitl n-2 

        n=len(word)
        freq=1
        for i in range(n-1):
            # print(word[i])
            if word[i]==word[i+1]:
                freq+=1
        return freq