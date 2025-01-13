class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valToIndexHash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in valToIndexHash:
                return [valToIndexHash[diff], i]
            valToIndexHash[n] = i