class Solution:
    @staticmethod
    def twoSum(num, targ):
        for i in range(len(num)):
            for j in range(i+1, len(num)):
                if num[i] + num[j] == targ:
                    print(f"[{i} ,{j}]")
                    return [i, j]
o = Solution().twoSum([3,3],6)
