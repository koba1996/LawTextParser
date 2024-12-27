import re


def parse_exp_line(line):
    number_range = re.split('\.? ', line)[1]
    if '-' in number_range:
        numbers = number_range.split('-')
        return int(numbers[1]) - int(numbers[0]) + 1
    else:
        return 1


def prepare_sections(law, explanation):
    law_file = open(law, "r", encoding="utf8")
    law_text = law_file.read()
    law_sections = re.split(r'\n\d+\. §.*\n', law_text)[1:]
    exp_file = open(explanation, "r", encoding="utf8")
    exp_text = exp_file.read()
    exp_sections_raw = re.split(r'(\nA[z]? \d+.* §-hoz\n)', exp_text)[1:]
    exp_sections = []
    i = 0
    while i < len(exp_sections_raw):
        limit = parse_exp_line(exp_sections_raw[i])
        i += 1
        for _ in range(limit):
            exp_sections.append(exp_sections_raw[i])
        i += 1
    return (law_sections, exp_sections)
