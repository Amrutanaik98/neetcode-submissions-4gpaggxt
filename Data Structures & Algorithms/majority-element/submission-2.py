class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x= nums.sort()
        return nums[len(nums)//2]