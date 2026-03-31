class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        CountMap = {}
        for n in nums:
            if n in CountMap:
                return True
            CountMap[n] = 1
        return False