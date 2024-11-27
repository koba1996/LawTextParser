import numpy as np

MATCH_START = '\033[91m'
MATCH_END = '\033[0m'

class Match:
    def __init__(self, first_start, first_end, second_start, second_end):
        self.first_start = first_start
        self.first_end = first_end
        self.second_start = second_start
        self.second_end = second_end

    def __repr__(self) -> str:
        return f'({self.first_start}, {self.first_end}, {self.second_start}, {self.second_end})'
    
    def __eq__(self, other):
        if isinstance(other, Match):
            return self.first_start == other.first_start and self.first_end == other.first_end or self.second_start == other.second_start and self.second_end == other.second_end
        return False
    
    def __hash__(self):
        return hash((self.first_start, self.first_end, self.second_start, self.second_end))


def find_longest_common_substring(first: str, second: str) -> tuple:
    matrix = np.zeros((len(first), len(second)))
    length = 0
    indexes = set()
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > length:
                    length = matrix[i][j]
                    indexes = set()
                    indexes.add(Match(int(i - length + 1), i, int(j - length + 1), j))
                elif matrix[i][j] == length:
                    indexes.add(Match(int(i - length + 1), i, int(j - length + 1), j))
            else:
                matrix[i][j] = 0
    return indexes


def compare_strings():
    pass


def format_output(str1, str2, matches):
    str1_parts = set()
    str2_parts = set()
    str1_formatted = ''
    str2_formatted = ''
    index1 = 0
    index2 = 0
    for match in matches:
        start_index1 = match.first_start
        start_index2 = match.second_start
        end_index1 = match.first_end
        end_index2 = match.second_end
        part_str_rep1 = str(start_index1) + '-' + str(end_index1)
        part_str_rep2 = str(start_index2) + '-' + str(end_index2)
        if part_str_rep1 in str1_parts or part_str_rep2 in str2_parts:
            continue
        str1_parts.add(part_str_rep1)
        str2_parts.add(part_str_rep2)
        str1_formatted += str1[index1:start_index1] + MATCH_START + str1[start_index1:end_index1 + 1] + MATCH_END
        index1 = end_index1 + 1
        str2_formatted += str2[index2:start_index2] + MATCH_START + str2[start_index2:end_index2 + 1] + MATCH_END
        index2 = end_index2 + 1
    str1_formatted += str1[index1:]
    str2_formatted += str2[index2:]
    return (str1_formatted, str2_formatted)

str1 = 'ahaccahac'
str2 = 'bahabahab'
result = format_output(str1, str2, find_longest_common_substring(str1, str2))
print(result[0])
print(result[1])