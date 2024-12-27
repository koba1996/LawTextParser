MATCH_START = '\033[91m'
MATCH_END = '\033[0m'
MINIMUM_MATCH_LENGTH = 7


class Compared_Strings:

    def __init__(self, str1, str2, index1, index2):
        self.str1 = str1
        self.str2 = str2
        self.index1 = index1
        self.index2 = index2


def create_matrix_with_zeros(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        matrix.append(row)
    return matrix


def is_distinct_interval(interval, prev_intervals):
    for prev_interval in prev_intervals:
        if prev_interval[0] <= interval[0] <= prev_interval[1] or prev_interval[0] <= interval[1] <= prev_interval[1]:
            return False
    return True


def filter_overlapping(indexes: list) -> list:
    first_pairs = []
    second_pairs = []
    unique_indexes = []
    for index_pair in indexes:
        first = [index_pair[0], index_pair[1]]
        second = [index_pair[2], index_pair[3]]
        if is_distinct_interval(first, first_pairs) and is_distinct_interval(second, second_pairs):
            unique_indexes.append(index_pair)
            first_pairs.append(first)
            second_pairs.append(second)
    return unique_indexes


def find_longest_common_substring(first: str, second: str) -> list:
    if len(first) < MINIMUM_MATCH_LENGTH or len(second) < MINIMUM_MATCH_LENGTH:
        return []
    matrix = create_matrix_with_zeros(len(first), len(second))
    length = 0
    indexes = []
    for i in range(len(first)):
        for j in range(len(second)):
            if first[i] == second[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > length:
                    length = matrix[i][j]
                    indexes = []
                    indexes.append([int(i - length + 1), i, int(j - length + 1), j])
                elif matrix[i][j] == length:
                    indexes.append([int(i - length + 1), i, int(j - length + 1), j])
            else:
                matrix[i][j] = 0
    if len(indexes) == 0 or indexes[0][1] - indexes[0][0] + 1 < MINIMUM_MATCH_LENGTH:
        return []
    return filter_overlapping(indexes)


def split_strings(first: str, second: str, index_pairs: list, first_offset=0, second_offset=0) -> list:
    if len(index_pairs) == 0:
        return []
    result = [{
        "first_str": first[:index_pairs[0][0]],
        "second_str": second[:index_pairs[0][2]],
        "first_index": first_offset,
        "second_index": second_offset
    }]
    for i in range(len(index_pairs)):
        if i != len(index_pairs) - 1:
            result.append({
                "first_str": first[index_pairs[i][1] + 1:index_pairs[i + 1][0]],
                "second_str": second[index_pairs[i][3] + 1:index_pairs[i + 1][2]],
                "first_index": index_pairs[i][1] + 1 + first_offset,
                "second_index": index_pairs[i][3] + 1 + second_offset
            })
        else:
            result.append({
                "first_str": first[index_pairs[i][1] + 1:],
                "second_str": second[index_pairs[i][3] + 1:],
                "first_index": index_pairs[i][1] + 1 + first_offset,
                "second_index": index_pairs[i][3] + 1 + second_offset
            })
    return result


def compare_strings(first: str, second: str, first_offset=0, second_offset=0):
    index_pairs = find_longest_common_substring(first, second)
    if len(index_pairs) == 0:
        return []
    str_parts = split_strings(first, second, index_pairs, first_offset, second_offset)
    for i in range(len(index_pairs)):
        index_pairs[i][0] += first_offset
        index_pairs[i][1] += first_offset
        index_pairs[i][2] += second_offset
        index_pairs[i][3] += second_offset
    position = 0
    for str_part in str_parts:
        sub_index_pairs = compare_strings(str_part["first_str"], str_part["second_str"], str_part["first_index"], str_part["second_index"])
        if position < len(index_pairs):
            index_pairs = index_pairs[:position] + sub_index_pairs + index_pairs[position:]
            position += len(sub_index_pairs) + 1
        else:
            index_pairs = index_pairs[:position] + sub_index_pairs
    return index_pairs


def get_first_index(index_pair):
    return index_pair[0]


def prepare_match_object(first: str, second: str, index_pairs: list) -> Compared_Strings:
    first_str_indexes = []
    second_str_indexes = []
    for index_pair in index_pairs:
        first_str_indexes.append(index_pair[:2])
        second_str_indexes.append(index_pair[2:])
    first_str_indexes = sorted(first_str_indexes, key=get_first_index)
    second_str_indexes = sorted(second_str_indexes, key=get_first_index)
    return Compared_Strings(first, second, first_str_indexes, second_str_indexes)


def perform_full_compare(first: str, second: str) -> Compared_Strings:
    return prepare_match_object(first, second, compare_strings(first, second))
