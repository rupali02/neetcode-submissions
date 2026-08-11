# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def max_path(root):
            if root is None:
                return 0, float('-inf')

            left_path, left_sum = max_path(root.left)
            right_path, right_sum = max_path(root.right)

            cur_path = root.val + max(0, left_path, right_path)
            cur_sum = max(left_sum, right_sum, root.val + max(0, left_path, right_path, left_path + right_path))

            return cur_path, cur_sum

        _, res = max_path(root)
        return res
        