class Solution:
    @staticmethod
    def twoSum(num, targ):
        for i in range(len(num)):
            for j in num:
                if i + j == targ:
                    print(f"[{num.index(i)} ,{num.index(j)}]")
                    return [num.index(i) ,num.index(j)]
o = Solution().twoSum([3,3],6)
