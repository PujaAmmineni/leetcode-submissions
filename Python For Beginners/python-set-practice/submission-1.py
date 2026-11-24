from typing import List

def contains_duplicate(words: List[str]) -> bool:
    count=[]
    for word in range(len(words)):
        if words[word] in count:
            return True
        else:
            count.append(words[word])
    return False
    


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
