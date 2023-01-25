class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        values={}
        for num in nums:
            if num in values:
                del values[num]
            else:
                values[num] = 1
        return list(values.keys())[0]
        