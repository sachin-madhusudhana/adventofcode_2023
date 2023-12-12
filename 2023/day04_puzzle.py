import re
import numpy as np

cards = open('december_4_input.txt').readlines()

# Part 1
""" total = 0

for match in data:
    card = match.split(':')[1]

    lucky_num = card.split("|")[0]
    chances = card.split("|")[1]

    lucky_num_list = [int(num) for num in lucky_num.split()]
    chances_list = [int(num) for num in chances.split()]
    print(lucky_num_list)
    initial_price = 1
    price = 0
    first_match = True
    for i, val in enumerate(lucky_num_list):
        if val in chances_list:
            if first_match:
                price = initial_price
                first_match = False

            else:
                price *= 2

    total += price

print(total) """

# Part 2

#%%

count = 0
multiplier = np.ones(len(cards))

for i, card in enumerate(cards):
    card = card.split(":")[1].split("|")

    # Parse the winning and have sets
    winning = set([int(x) for x in card[0].strip().split()])
    lucky_num = set(int(x) for x in card[1].strip().split())

    wins = winning.intersection(lucky_num)

    # Get the multiplier for this card
    cmultiplier = multiplier[i]

    print(min(i + len(wins) + 1, len(cards)))
    for j in range(i + 1, min(i + len(wins) + 1, len(cards))):
        
        multiplier[j] += cmultiplier

    count += cmultiplier

print(count)