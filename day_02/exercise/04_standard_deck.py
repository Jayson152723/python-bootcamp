ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
suits = ("Hearts", "Diamonds", "Clubs", "Spades")
deck = []

deck = [f"{rank} of {suit}" for rank in ranks for suit in suits]
print(deck)
