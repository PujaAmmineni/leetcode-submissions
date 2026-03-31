class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s  # Store length and string with separator
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):  # Use s, not str
            j = i
            while s[j] != '#':  # Find the delimiter
                j += 1
            length = int(s[i:j])  # Get length of string
            res.append(s[j+1 : j+1+length])  # Extract string using length
            i = j + 1 + length  # Move pointer forward
        return res
