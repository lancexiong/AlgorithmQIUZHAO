#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(0,len(prices)-1):
            j=i+1
            if prices[j]<prices[i]:
                continue
            buy=prices[i]
            sale=prices[j]
            profit+=(sale-buy)
        return profit
# @lc code=end

