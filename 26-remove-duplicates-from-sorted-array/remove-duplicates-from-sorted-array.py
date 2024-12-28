class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        
        for l in range(1, len(nums)):
            if nums[l] != nums[l-1]:
                nums[k] = nums[l]
                k += 1
        
        return k
