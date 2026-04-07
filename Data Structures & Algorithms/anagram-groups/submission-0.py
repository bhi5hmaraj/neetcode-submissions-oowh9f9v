from collections import defaultdict 
class Solution:
    def hash(self, word: str) -> List[int]:
        cnt = [0] * 26
        for i in range(len(word)):
            cnt[ord(word[i]) - ord('a')] += 1
        
        return '-'.join(map(str, cnt))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupby = defaultdict(list)
        for word in strs:
            groupby[self.hash(word)].append(word)
        
        return [v for v in groupby.values()]