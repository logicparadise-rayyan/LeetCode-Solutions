class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_string = ""
        for num in digits:
            num_string = num_string + str(num)
            final_num = int(num_string) + 1
            final_string = str(final_num)
            convert_string_to_list = list(final_string)
        final_list = []
        nums=0
        while nums < len(convert_string_to_list):
            number = int(convert_string_to_list[nums])
            final_list.append(number)
            nums+=1
        return (final_list)