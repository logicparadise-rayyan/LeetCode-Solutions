class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=['']*len(s)
        for nums in range(len(indices)):
            res[indices[nums]]= s[nums]
        return "".join(res)