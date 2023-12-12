import re
import os

number_mapping = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

data = open('day01.txt', 'r').read().split('\n')
calibration_values_sorted = []
map_dict = {}
#%%
# Part 1
"""
for values in data:
    matches = re.findall(r'\d', values)
    calibration_values_sorted.append(int(''.join(matches[0] + matches[-1]))) """

#%%

# Part 2


def append_string(alpha):
    joined_word = ''.join(alpha)
    found_values = {}
    for value in number_mapping.keys():
        if value in joined_word:
            substring = joined_word.count(value)            
            idd = 0
            found_values[value] = []
            for val in range(substring):
                idd =  joined_word.find(value, idd)
                found_values[value].append(idd)
                idd = idd + 1

    if len(found_values.keys()) > 1:
        sorted_tuples = [(key, sorted(indices)) for key, indices in found_values.items()]

        sorted_list = sorted([(key, index) for key, indices in sorted_tuples for index in indices], key=lambda x: x[1])
        output_array = [key for key, _ in sorted_list]
        for out in output_array:
            lst.append(str(number_mapping[out]))

    else:
        for key, item in found_values.items():
            for r in range(len(item)):
                lst.append(str(number_mapping[key]))

for values in data:
    all_num = []
    lst = []
    alpha = []
    x = re.findall("\w", values)

    for i, jj  in enumerate(x):
        if jj.isdigit():
            if (alpha):
                append_string(alpha)
                alpha.clear()
            lst.append(jj)
        else:
            alpha += jj
            if len(values)-1 == i:
                append_string(alpha)
    joint_value = int(''.join(lst[0] + lst[-1]))
    map_dict[values] = joint_value
    calibration_values_sorted.append(joint_value)


print(sum(calibration_values_sorted))