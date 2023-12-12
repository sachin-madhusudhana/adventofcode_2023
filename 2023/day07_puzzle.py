#%%
import numpy as np
from collections import Counter

data = open('day07.txt').read().split('\n')

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []
#%%
# Part 1
# values_part1 = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Part 2
values_part2 = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}


def custom_sort(element):
    return tuple(values_part2[char] for char in element[0])

def sorted_bid(type, rank):
    hand_bid = []
    sorted_cards = sorted(type, key=custom_sort)
    for i, val in enumerate(sorted_cards):
        hand_bid.append(rank * int(val[1]))
        rank += 1
    return sum(hand_bid), rank

def add_to_type(unique_card_counter, hand, bid):
    if len(unique_card_counter) == 5:
        high_card.append([hand, bid])
    if len(unique_card_counter) == 4:

        one_pair.append([hand, bid])

    if len(unique_card_counter) == 3:
        max(unique_card_counter)
        if max(unique_card_counter) == 3:
            three_of_a_kind.append([hand, bid])
        else:
            two_pair.append([hand, bid])
    if len(unique_card_counter) == 2:
        if(max(unique_card_counter)) == 4:
            four_of_a_kind.append([hand, bid])
        else:
            full_house.append([hand, bid])
    if len(unique_card_counter) == 1:
        five_of_a_kind.append([hand, bid])


#%%
for hand_bid in data:
    hand = hand_bid.split()[0]
    bid = hand_bid.split()[1]
    unique_cards = Counter(hand).keys()
    joker_counter = hand.count("J")
    removing_joker = hand.replace("J","")
    unique_card_counter = sorted(Counter(removing_joker).values(),reverse=True)
    if joker_counter > 0:
        if unique_card_counter:
            val = list(unique_card_counter)[0] + joker_counter
        else:
            val = 5
        if val == 2:
            one_pair.append([hand,bid])
        if val == 3 and list(unique_card_counter)[1] == 2:
            full_house.append([hand,bid])
        if val == 3 and list(unique_card_counter)[1] == 1:
            three_of_a_kind.append([hand,bid])
        if val==4:
            four_of_a_kind.append([hand,bid])
        if val==5:
            five_of_a_kind.append([hand,bid])   
    else:
        add_to_type(unique_card_counter, hand, bid)


sum_high_card, rank = sorted_bid(high_card, rank=1)
sum_one_pair, rank = sorted_bid(one_pair, rank)
sum_two_pair, rank = sorted_bid(two_pair, rank)
sum_three_of_a_kind, rank = sorted_bid(three_of_a_kind, rank)
sum_full_house, rank = sorted_bid(full_house, rank)
sum_four_of_a_kind, rank = sorted_bid(four_of_a_kind, rank)
sum_five_of_a_kind, rank = sorted_bid(five_of_a_kind, rank)

print(sum_high_card + sum_one_pair + sum_two_pair + sum_three_of_a_kind 
      + sum_full_house + sum_four_of_a_kind + sum_five_of_a_kind)
