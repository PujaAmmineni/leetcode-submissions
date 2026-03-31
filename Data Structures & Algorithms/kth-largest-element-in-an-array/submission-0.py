import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k

        def quickselect(l,r):
            pivot=random.randint(l,r)
            nums[pivot],nums[r]=nums[r],nums[pivot]

            p=l
            for i in range(l,r):
                if nums[i]<=nums[r]:
                    nums[i],nums[p]=nums[p],nums[i]
                    p+=1


            nums[p],nums[r]=nums[r],nums[p]

            if p<k:
                return quickselect(p+1,r)
            elif p>k:
                return quickselect(l,p-1)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)
        