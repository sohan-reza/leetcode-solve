class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        mp = defaultdict(int)
        for x in nums:
            mp[x]+=1
        return list(dict(sorted(mp.items(), key=lambda item: item[1], reverse=True)).keys())[:k]
            
