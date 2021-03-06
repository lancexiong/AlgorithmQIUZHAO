#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
class Solution:
 
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n<1:
            return []
        self.result=[]
        self.cols=set()
        self.pie=set()
        self.na=set()
        self.dfs(n,0,[])
        return self._generate_result(n)
    def dfs(self,n,row,current_sate):
        if n==row:
            self.result.append(current_sate)
        for col in range(n):
            if col in self.cols or col+row in self.pie or row-col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row+col)
            self.na.add(row-col)
            self.dfs(n,row+1,current_sate+[col])
            self.cols.remove(col)
            self.pie.remove(row+col)
            self.na.remove(row-col)
    def _generate_result(self,n):
        board=[]
        for res in self.result:
            for i in res:
                board.append('.'*i+'Q'+(n-i-1)*'.')
        return [board[i:i+n] for i in range(0,len(board),n)]

    



# @lc code=end

