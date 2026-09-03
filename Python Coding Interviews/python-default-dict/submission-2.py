from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    s1=defaultdict(int)
    for i in s:
        s1[i]+=1
    return s1



def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    l=defaultdict(list)
    for i in nums:
        for j in i[1:]:
            l[i[0]].append(j)
    return l

    for num in nums:
        l1[num[0]].append(num[1:])
    return l1

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
