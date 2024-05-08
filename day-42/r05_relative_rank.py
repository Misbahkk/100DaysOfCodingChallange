"""You are given an integer array score of size n, where score[i] 
is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place 
athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. 
The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete."""

class Solution(object):
    def findRelativeRanks(self,score):
        #your code
        score_rank = []
        score_rank = sorted(score, reverse=True)
        
        # score_rank[0] = "Gold Medal"
        # score_rank[1]="Silver Medal"
        # score_rank[2]="Bronze Medal"
        rank_dic ={}
        for i ,score in enumerate(score_rank):
            if i<3:
                if i ==0:
                    rank_dic[score]='Gold Medal'
                elif i == 1:
                    rank_dic[score] ='Silver Medal'
                else:
                    rank_dic[score]="Bronze Medal"
            else:
                rank_dic[score_rank[i]] = str(i+1)

        
        return rank_dic
            

            
            

            





score= [10,3,5,8,2]
obj = Solution()
score_rank = obj.findRelativeRanks(score)
rank = [score_rank[s] for s in score]
print(rank)