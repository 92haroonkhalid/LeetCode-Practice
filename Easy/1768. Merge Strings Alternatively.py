class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = word1
        b = word2
        l = []
        for i in range(max(len(a), len(b))):
            if i<len(a):
                l.append(a[i])
            if i<len(b):
                l.append(b[i])
        result = ''.join(l)
        print(result)
o = Solution()
o.mergeAlternately("abc","pqr")
