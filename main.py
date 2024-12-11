from string_compare import perform_full_compare
from output_formatter import format_output


str1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."
str2 = "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
match_object = perform_full_compare(str1, str2)
formatted_output = format_output(match_object)
print(formatted_output[0])
print(formatted_output[1])