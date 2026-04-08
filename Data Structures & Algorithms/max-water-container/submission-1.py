class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(len(heights)):
            for j in range(0, i, 1):
                if heights[j] >= heights[i]:
                    ans = max(ans, (i - j) * heights[i])
                else:
                    ans = max(ans, (i - j) * heights[j])
        return ans
