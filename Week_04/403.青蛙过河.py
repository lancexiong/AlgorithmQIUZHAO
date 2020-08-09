#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] 青蛙过河
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        从开始位置出发，记录每一步跳转到第i个石头所用的步数step,然后newstep
        in (step-1,step,step+1)，若stones[i]+newstep扔在stones中，则
        在newpoint记录此newstep，最后看最后一个石子是否有步数step
        '''
        n=len(stones)
        dic={}
        for i in stones:
            dic[i]=set()
        for i in range(n):
            if i ==0:
                dic[stones[i]].add(0)
            for j in dic[stones[i]]:
                for k in range(j-1,j+2) :
                    if k!=0 and stones[i]+k in dic:
                        dic.get(stones[i]+k).add(k)
        return len(dic[stones[-1]])>0
# @lc code=end

