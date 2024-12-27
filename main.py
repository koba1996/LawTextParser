from string_compare import perform_full_compare
from output_formatter import format_output
from sentence_breaker import prepare_sections

law, explanation = prepare_sections("torveny.txt", "indoklas.txt")
for i in range(min(len(law), len(explanation))):
    str1 = law[i]
    str2 = explanation[i]
    match_object = perform_full_compare(str1, str2)
    if len(match_object.index1) > 0:
        formatted_output = format_output(match_object)
        print(formatted_output[0])
        print("--------------------------------------------")
        print(formatted_output[1])
        print("============================================")