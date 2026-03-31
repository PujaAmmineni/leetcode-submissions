

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset, curset = [], []
        self.helper(0, nums, subset, curset)
        return subset

    def helper(self, i, nums, subset, curset):
        if i >= len(nums):
            subset.append(curset.copy())
            return

        # Decision NOT to include nums[i]
        self.helper(i + 1, nums, subset, curset)

        # Decision to include nums[i]
        curset.append(nums[i])
        self.helper(i + 1, nums, subset, curset)
        curset.pop()  # backtrack
