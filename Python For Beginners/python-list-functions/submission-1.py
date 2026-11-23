from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    count_sum=0
    for i in nums:
        count_sum+=i
    return count_sum
    

def get_min(nums: List[int]) -> int:
    count_min=nums[0]
    for i in nums:
        if i<count_min:
            count_min=i
    return count_min



    

def get_max(nums: List[int]) -> int:
    count_max=0
    for i in nums:
        if i> count_max:
            count_max=i
    return count_max
    

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
