#%%
import re

data = open('day03.txt').read().split('\n')

# part 1
not_part_numbers = []
part_numbers = []
gears = []
associated_symbols = []


initial_i = 0
lr = "L"
for i, line in enumerate(data):
    only_digits = re.findall(r'[0-9]+', line)
    idx = 0
    for dig in only_digits:
        sym_idx = 0
        idx = line.find(dig, idx)
        if idx==0:
            adjacent_values = ''.join(line[len(dig)])
            diag_left = idx
            lr = "R"
        else:
            diag_left = idx - 1

        if idx+len(dig) == len(line):
            lr = "L"
            adjacent_values = ''.join(line[idx-1])
            diag_right = idx+len(dig)
        else:
            diag_right = idx+len(dig) + 1
        
        if idx != 0 and idx+len(dig) != len(line):
            lr = "LR"
            adjacent_values = ''.join(line[idx-1] + line[len(dig)+idx])


        if len(re.findall("[.]", adjacent_values)) < len(adjacent_values):
            if (re.findall("[*]", adjacent_values)):
                sym_idx = adjacent_values.find("*", sym_idx)
                if lr == "L":
                    associated_symbols.append(f"{i}_{idx-1}_{dig}")
                elif lr == "R":
                    associated_symbols.append(f"{i}_{len(dig)+idx}_{dig}")
                elif sym_idx == 0:
                    associated_symbols.append(f"{i}_{idx-1}_{dig}")
                else:
                    associated_symbols.append(f"{i}_{len(dig)+idx}_{dig}")
            part_numbers.append(int(dig))
            idx = idx + len(dig)
            continue
        if i != 0:
            prev_row = data[i-1][diag_left:diag_right]
            if len(re.findall("[.]", prev_row)) < len(prev_row):
                part_numbers.append(int(dig))
                if (re.findall("[*]", prev_row)):
                    sym_idx = prev_row.find("*", sym_idx)
                    idx = idx + len(dig)
                    associated_symbols.append(f"{i-1}_{diag_left + sym_idx}_{dig}")
                continue
        if i != len(data)-1:
            nxt_row = data[i+1][diag_left:diag_right]
            if len(re.findall("[.]", nxt_row)) < len(nxt_row):
                part_numbers.append(int(dig))
                idx = idx + len(dig)
                if (re.findall("[*]", nxt_row)):
                    sym_idx = nxt_row.find("*", sym_idx)
                    associated_symbols.append(f"{i+1}_{diag_left+sym_idx}_{dig}")
                continue
        not_part_numbers.append(int(dig))
        idx = idx + len(dig) + 1
        

gears = []

for idx_i in range(0, len(associated_symbols)):
    i = associated_symbols[idx_i].split('_')[0]
    star_i = associated_symbols[idx_i].split('_')[1]
    part_i = associated_symbols[idx_i].split('_')[2]
    idx_j = idx_i
    while idx_j != len(associated_symbols)-1:

        j = associated_symbols[idx_j+1].split('_')[0]
        if (j == i):
            star_j = associated_symbols[idx_j+1].split('_')[1]
            if star_i == star_j:
                part_j = associated_symbols[idx_j+1].split('_')[2]
                gears.append(int(part_i) * int(part_j))
                break
        idx_j += 1

print("Part 1 : ", sum(part_numbers))
print("Part 2 : ",sum(gears))
