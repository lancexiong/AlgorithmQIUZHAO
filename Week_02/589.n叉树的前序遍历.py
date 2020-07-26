#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        L=[]
        def helper(root):
            if root is None:
                return root
            L.append(root.val)
            for i in root.children:
                L.extend(self.preorder(i))
            return L
        return helper(root)

        
# @lc code=end

