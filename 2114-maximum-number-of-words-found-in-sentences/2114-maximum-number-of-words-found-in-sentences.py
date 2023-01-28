class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentence_length=[]
        for sents in sentences:
            splitted_strings=sents.split()
            length_str = len(splitted_strings)
            sentence_length.append(length_str)
        return max(sentence_length)
        