class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str={}
        for string in strs:
            sorted_word = ''.join(sorted(string))
            if sorted_word in sorted_str:
                sorted_str[sorted_word].append(string)
            else:
                sorted_str[sorted_word]=[string]

        return list(sorted_str.values())
        