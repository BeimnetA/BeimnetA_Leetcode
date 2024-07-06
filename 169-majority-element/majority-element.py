class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        
        # Loop over the array. Add number to the hash table 
        for num in nums:
            if num in hashtable.keys():
                hashtable[num] += 1  
            else:
                hashtable[num] = 1 
            
            # If the number of counts reach n/2 + 1 return that number
            if hashtable[num] > (len(nums) / 2):
                return num