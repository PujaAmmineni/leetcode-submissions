from typing import List

def read_integers() -> List[int]:
    user=input()
    strings=user.split(",")
    result=[]
    for s in strings:
        result.append(int(s))
    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
