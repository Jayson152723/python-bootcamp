from random import choice

ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
deck = []

def create_deck():
    deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
    return deck

def draw_top(deck: list[str], count: int=1)-> list[str]:
    draw = deck.pop(0)
    return draw

def draw_bottom(deck: list[str], count: int=1) -> list[str]:
    draw = deck.pop(-1)
    return draw

def draw_random(deck: list[str], count: int=1) -> list[str]:
    random_option = choice(deck)
    deck.remove(random_option)
    return random_option

def show(deck):
    print(deck)
deck = create_deck()
print(draw_top(deck))
print(draw_bottom(deck))
print(draw_random(deck))
show(deck)
