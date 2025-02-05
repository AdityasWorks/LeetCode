class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        b = 1
        while b!= len(nums):
            if nums[a] != nums[b]:
                a+=1
                nums[a] = nums[b]
            b+=1
            
        return a+1