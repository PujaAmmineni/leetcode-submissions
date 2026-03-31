class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0  # Count of visited nodes
        stack = []  # Stack for in-order traversal
        curr = root  # Start traversal from root

        while curr or stack:
            while curr:
                stack.append(curr)  # Go as left as possible
                curr = curr.left

            curr = stack.pop()  # Visit the node
            n += 1  # Increase the counter

            if n == k:
                return curr.val  # Found kth smallest

            curr = curr.right  # Now check the right subtree
