from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = defaultdict(list)  # Map character count → list of anagrams

        for s in strs:               # For each string in input
            count = [0] * 26         # 26-letter count for a-z

            for c in s:              # Count each character
                count[ord(c) - ord('a')] += 1

            sublist[tuple(count)].append(s)  # Use char count as key to group
          
        return list(sublist.values())
