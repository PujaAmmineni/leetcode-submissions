def remove_fourth_character(word: str) -> str:
    fourth=word[:3]
    remain=word[4:]
    return fourth+remain


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
