import re

data = open('day_02.txt', 'r').read().split('\n')
#%%
# Part 1
total = 0
for i, game in enumerate(data):
    green = 0
    blue = 0
    red_c = 0
    flag = True
    x = game.split(':')
    y = x[1].split(";")
    for val in y:
        gr = re.findall(r'(\d+\s)green', val)
        bl= re.findall(r'(\d+\s)blue', val)
        red = re.findall(r'(\d+\s)red', val)
    
        if gr:
            if (int(gr[0]) > 13):
                flag = False
                break
            else:
                green += int(gr[0])
        if bl:
            if (int(bl[0]) > 14):
                flag = False
                break
            else:
                blue += int(bl[0])
        if red:
            if (int(red[0]) > 12):
                flag = False
                break
            else:
                red_c += int(red[0])
    if flag:
        total += i+1 




print(total)
#%%

# Part 2

total = []

for i, game in enumerate(data):
    green = []
    blue = []
    red_c = []
    flag = True
    x = game.split(':')
    y = x[1].split(";")
    for val in y:
        gr = re.findall(r'(\d+\s)green', val)
        bl= re.findall(r'(\d+\s)blue', val)
        red = re.findall(r'(\d+\s)red', val)

        if gr:
            green.append(int(gr[0]))
        if bl:
            blue.append(int(bl[0]))
        if red:
            red_c.append(int(red[0]))
    if not green:
        total.append(max(blue) * max(red))
    
    if not blue:
        total.append(max(green) * max(red))
    
    if not red_c:
        total.append(max(green) * max(blue))
    
    else:
        total.append(max(green) * max(blue) * max(red_c))

print(sum(total))
