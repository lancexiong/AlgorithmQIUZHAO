#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(string,left,right,params=[]):
            if left >0:
                generate(string+'(',left-1,right)
            if right > left:
                generate(string+')',left,right-1)
            if right==0:
                params.append(string)
            return params
        return generate('',n,n)
            
# @lc code=end

