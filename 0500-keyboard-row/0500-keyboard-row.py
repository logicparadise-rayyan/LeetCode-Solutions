class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1= "qwertyuiop"
        r2= "asdfghjkl"
        r3= "zxcvbnm"
        res=[]
        for w in words:
            word=w.lower()
            if len(set(r1+word))==len(r1) or len(set(r2+word))==len(r2)  or len(set(r3+word))==len(r3):
                res.append(w)
        return res