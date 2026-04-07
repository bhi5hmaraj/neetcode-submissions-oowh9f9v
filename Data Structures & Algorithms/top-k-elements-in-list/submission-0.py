from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        cnt_tuples = list(cnt.items())
        cnt_tuples.sort(key=lambda kv: kv[1], reverse=True)
        print(cnt_tuples)
        cnt_tuples_sorted_topk = cnt_tuples[:k]
        print(cnt_tuples_sorted_topk)
        return list(map(lambda kv: kv[0], cnt_tuples_sorted_topk)) 