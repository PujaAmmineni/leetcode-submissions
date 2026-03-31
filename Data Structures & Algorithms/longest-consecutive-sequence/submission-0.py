class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for n in nums:
            #checking if its a start of sequence
            if(n-1) not in numSet:
                length=0 #length of sequence is 0
                while(n+length) in numSet:#checking current number intially length is 0
                    length+=1 
                longest=max(length,longest)
        return longest



        