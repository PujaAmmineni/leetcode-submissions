class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            # width = r - l
            # height of container = min(height[l], height[r])
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            # Move the pointer with the shorter line inward
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  # ← You had r += 1, but we need r -= 1

        return res
