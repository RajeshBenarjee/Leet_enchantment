class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        left=0
        right=0
        n=len(players)
        m=len(trainers)
        players.sort()      # ---O(NlogN)
        trainers.sort()     # ---O(NlogN)
        count=0
        while left<n and right<m:   #---O(min(n,m))
            if players[left]<=trainers[right]:
                count+=1
                left+=1
                right+=1
            else:
                right+=1
        return count 