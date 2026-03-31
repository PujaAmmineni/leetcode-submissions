class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True    # Empty subRoot is always a subtree
        if not root:
            return False   # Non-empty subRoot can't be subtree of empty tree

        # If trees match at this node, return True
        if self.sameTree(root, subRoot):
            return True

        # Recur down the main tree: look in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True    # Both trees empty → match

        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))

        return False    # Mismatch or structure doesn't align
