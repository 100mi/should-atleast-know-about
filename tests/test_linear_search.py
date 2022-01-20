import pytest
from dsa.linear_search import locate_cards

DECK = [13, 11, 10, 7, 4, 3, 1, 0]
DUPLIATED_DECK = [13,13,9,9,9,9,7,7,4,3,2,2,1]
SINGLE_DECK = [1]
NULL_DECK = []

@pytest.mark.parametrize(
    "deck,card,expeted_position",
    [
        (DECK, 7, 4),
        (DECK, 13, 1),
        (DECK, 0, 8),
        (SINGLE_DECK, 1, 1),
        (NULL_DECK, 4, -1),
        (DECK, 2, -1),
        (DUPLIATED_DECK, 9, 3),
        (DUPLIATED_DECK, 4, 9)

    ]
)
def test_locate_cards(deck, card, expeted_position):
    assert locate_cards(deck, card) == expeted_position