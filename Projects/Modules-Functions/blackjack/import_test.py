import blackjack
#from blackjack import * # everything from blackjack loads into this file's namespace (except _functions)

#print('\n', __name__, '\n')

# modules that start with '_' are likely intended to be private (not public access)
#blackjack._deal_card(blackjack.dealer_card_frame) # no private/public variable protection
#blackjack.play()
#print(blackjack.cards)

# g = sorted(globals())
# #for x in globals(): # doesn't work b/c x creates new variable
# for x in g: 
#     print(x)

personal_details = ("Tim", 24, "Australia")

name, _, country = personal_details # _ is throw-away value
print(name, country)
print(_)