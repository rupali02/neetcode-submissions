class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max, cur_min = 1, 1
        res = float('-inf')

        for num in nums:
            tmp = max(num, cur_max * num, cur_min * num)
            res = max(res, tmp)
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = tmp

        return res
        