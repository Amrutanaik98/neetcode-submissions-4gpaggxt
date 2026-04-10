class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp=[]
        for i in nums:
            if i==val:
                continue
            tmp.append(i)
        for j in range(len(tmp)):
            nums[j] = tmp[j]
        return len(tmp)