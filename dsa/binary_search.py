from typing import List

def locate_cards(deck:List, card:int, turns = 0) -> int:

    position = (len(deck) -1) // 2
    
    if len(deck) == 0 :
        return -1
    
    elif deck[position] == card :
        return turns +1 

    elif deck[position] > card :
        return locate_cards(
            deck[position+1:], card, turns+1 
        )
    
    elif deck[position] < card : 
        return locate_cards(
            deck[:position], card, turns+1
        )