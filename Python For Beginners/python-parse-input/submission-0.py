from typing import List

def read_integers() -> List[int]:
    read=input()
    nums=read.split(",")
    result=[]

    for i in nums:
        result.append(int(i))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
