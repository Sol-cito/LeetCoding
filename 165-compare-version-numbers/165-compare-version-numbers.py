class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(max(len(v1), len(v2))):
            a = int(v1[i]) if len(v1) > i else 0
            b = int(v2[i]) if len(v2) > i else 0
            if a > b: return 1
            if a < b: return -1
        return 0