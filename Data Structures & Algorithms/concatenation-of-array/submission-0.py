class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[] 
        for i in range(2):
            for vals in nums: 
                ans.append(vals)
        return ans
    
        