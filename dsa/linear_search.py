from typing import List

def locate_cards(deck: List, card: int) -> int:
    # return position/index of the card in that list
    for position, each_card in enumerate(deck,1):
        if each_card == card :
            return position
    return -1