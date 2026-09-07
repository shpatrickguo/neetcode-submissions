class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in hmap:
                return [hmap[diff], i]
            hmap[v] = i
