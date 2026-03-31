class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # For storing open parentheses
        closeToOpen = {")": "(", "]": "[", "}": "{"}  # Corrected: Opening for each closing

        for c in s:
            if c in closeToOpen:  # If it's a closing bracket
                # Check if stack is not empty AND top of stack matches expected opening
                if stack and stack[-1] == closeToOpen[c]:  #  use [c], not (c)
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)  # Push opening bracket to stack

        return True if not stack else False  # Stack must be empty at the end
