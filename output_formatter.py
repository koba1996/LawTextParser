from string_compare import Compared_Strings


MATCH_START = '\033[91m'
MATCH_END = '\033[0m'


def format_one_string(string, index_pairs):
    if len(index_pairs) == 0:
        return string
    formatted_string = ''
    formatted_string += string[:index_pairs[0][0]]
    for i in range(len(index_pairs)):
        formatted_string += MATCH_START + string[index_pairs[i][0]:index_pairs[i][1] + 1] + MATCH_END
        if i == len(index_pairs) - 1:
            formatted_string += string[index_pairs[i][1] + 1:]
        else:
            formatted_string += string[index_pairs[i][1] + 1:index_pairs[i + 1][0]]
    return formatted_string


def format_output(strings: Compared_Strings) -> tuple:
    first_formatted_string = format_one_string(strings.str1, strings.index1)
    second_formatted_string = format_one_string(strings.str2, strings.index2)
    return first_formatted_string, second_formatted_string