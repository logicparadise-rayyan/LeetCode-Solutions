class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        splitted = s.split()
        res = []
        string = 1
        for word in splitted:
            if len(res)!= k:
                res.append(word)
                string=string+1
        return " ".join(res)