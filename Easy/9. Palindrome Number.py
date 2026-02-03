class Solution:
    def isPalindrome(self, x):
        rev = 0
        a = 0
        temp = x
        while x > 0:
            rev = x % 10
            a = a * 10 + rev
            x = x // 10
        if temp == a:
            return True
        else:
            return False
x = Solution().isPalindrome(909)
