class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if sorted(s1[::2]) == sorted(s2[::2]) and sorted(s1[1::2]) == sorted(s2[1::2]):
            # print(True)
            return True
        return False