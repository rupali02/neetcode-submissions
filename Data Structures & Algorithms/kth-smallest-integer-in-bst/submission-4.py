# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findk(root, cnt):
            if root is None:
                return cnt, None

            cnt, left_val = findk(root.left, cnt)
            if left_val is not None:
                return cnt, left_val
            
            cnt += 1
            if cnt == k:
                return cnt, root.val

            cnt, right_val = findk(root.right, cnt)
            return cnt, right_val

        _, val = findk(root, 0)

        return val


        