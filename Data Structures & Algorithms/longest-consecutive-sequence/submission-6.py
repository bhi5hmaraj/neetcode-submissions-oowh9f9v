from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        for val in sorted(nums):
            memo[val] = max(memo[val], 1 if val - 1 not in memo else memo[val - 1] + 1)
        
        return max(memo.values()) if nums else 0
