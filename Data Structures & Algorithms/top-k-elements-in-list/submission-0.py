class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        f=Counter(nums)
        topk=[key for key,value in f.most_common(k)]
        return topk