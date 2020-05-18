# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def max_level_sum(self, root: TreeNode) -> int:
        levels = []
        queue = [root]

        level = 0
        while queue:
            new_queue = []
            for node in queue:
                levels[level] += node.val

                if node.right:
                    new_queue.append(node.right)
                if node.left:
                    new_queue.append(node.left)
            queue = new_queue
            level += 1

        return levels.index(max(levels))
