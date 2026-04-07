import functools

class Solution:
    # The solution is to precompute prefix and suffix product 
    # and combine them for the solution for each position
    # I will implement a purely functional solution using folds
    def precompute(self, nums) -> List[int]:
        return functools.reduce(lambda acc, x: acc + [acc[-1] * x], nums, [1])

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = self.precompute(nums)
        suffix_prod = list(reversed(self.precompute(reversed(nums))))
        print(prefix_prod, " -- ", suffix_prod)
        return list(map(lambda tup: tup[0] * tup[1], zip(prefix_prod, suffix_prod[1:])))
