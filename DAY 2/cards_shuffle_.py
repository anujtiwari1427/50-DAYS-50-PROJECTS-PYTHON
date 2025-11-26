import random 

suits = ['HEARTS','CLUBS','SPADES','DIAMOND']

ranks = ['2','3','4','5','6','7','8','9','10','JACK','KING','QUEEN','JOKER']

deck = [ r + " of " + s for s in suits for r in ranks ]

print("Original Deck Size:", len(deck))

print("The Shuffled Cards",random.shuffle(deck),deck)
