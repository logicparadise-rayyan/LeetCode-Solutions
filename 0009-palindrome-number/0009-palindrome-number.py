class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>0:
            unreversed_arr = list(map(int,str(x)))
            reversed_arr = unreversed_arr[::-1]
            if unreversed_arr == reversed_arr:
                return True
            else:
                return False
        elif x==0:
            return True
        else:
            return False

        