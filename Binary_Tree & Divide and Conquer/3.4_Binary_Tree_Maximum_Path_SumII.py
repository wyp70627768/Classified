"""
Description
=============
Given a binary tree, find the maximum path sum from root.
The path may end at any node in the tree and contain at least one node in it.

Example
=============
Example
Given the below binary tree:

  1
 / \
2   3
return 4. (1->3)
"""


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param root the root of binary tree.
    @return an integer
    """

    def maxPathSum2(self, root):
        # Write your code here
        if root is None:
            return 0
        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)

        return root.val + max(left, right, 0)
