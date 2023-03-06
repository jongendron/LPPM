#TODO: check if dealer has one each time
#TODO: add module to talley wins of dealer vs player
# How do we play the game with 2-3 packs of cards?
import random
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk


# Load Images Function
def load_images(card_images):
    suits = ['heart', 'club', 'diamond', 'spade']
    face_cards = ['jack', 'queen', 'king']

    if tk.TkVersion >= 8.6:
        extension = 'png'
    else:
        extension = 'ppm'

    # for eachc suit, retrieve the image for the cards
    for suit in suits:
        # first the number cards 1 to 10
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((card, image))

        # now face cards
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tk.PhotoImage(file=name)
            card_images.append((10, image))


# Deal cards function
def deal_card(frame):
    # pop the next card off top of the deck
    next_card = deck.pop(0) # save card variable and remove from list

    # put card back at bottom of deck (to reuse the same deck)
    deck.append(next_card)
    
    # add the image to the Label and display the label
    tk.Label(frame, image=next_card[1], relief='raised').pack(side='left') # pack can be used in its own window
    
    # now return the card's face value
    return next_card


# Score the hand
def score_hand(hand):
    # Calculate the total score of all cards in teh list.
    # Only one ace can have the value 11, and this will be reduced to 1 if the hand would bust.
    score = 0
    ace = False
    for next_card in hand:
        card_value = next_card[0]
        if card_value == 1 and not ace:
            ace = True
            card_value = 11
        score += card_value

        # if we would bust, check if there is an ace and subract 10
        if score > 21 and ace:
            score -= 10
            ace = False

    return score


# Deal dealer
def deal_dealer():
    #dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)
    
    player_score = score_hand(player_hand)
    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or dealer_score < player_score:
        result_text.set("Player wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    else:
        result_text.set("Draw!")


# Deal Player
def deal_player():
    # lists saved to global variables do not need to be defined in functions
    # these can be appended without being defined as global (and are meant to)
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)

    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    # # Once you try to assign new value to variable
    # #-> inside of a function -> function creates a local
    # global player_score # function uses global variable player_score instead of local
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1 and not player_ace:
    #     player_ace = True
    #     card_value = 11
    # player_score += card_value
    # # if we would bust, check if there is an ace and subtract
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")
    # #print('\n', locals(), '\n')


def shuffle():
    random.shuffle(deck)


def new_game():
    # 1. clears cards from screen
    #card_frame = tk.Frame(win, relief='sunken', borderwidth=1, background='green')
    #card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)
    global dealer_card_frame
    global player_card_frame

    dealer_card_frame.destroy()
    dealer_card_frame = tk.Frame(card_frame, background='green')
    dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)
    #dealer_card_frame.update()

    player_card_frame.destroy()
    player_card_frame = tk.Frame(card_frame, background='green')
    player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)
    #player_card_frame.update()

    # 2. reset's player and dealers hands
    global dealer_hand
    global player_hand
    dealer_hand = []
    player_hand = []
    result_text.set("")

    # 3. starts new hand
    # if you want new deck
    #global deck
    #deck = list(cards) if you want new deck
    #random.shuffle(deck)
    
    # if you want to just shuffle
    shuffle()

    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()


win = tk.Tk()

# Setup the screen and frames for the dealer and player
win.title("Blackjack")
win.geometry("640x480")
win.configure(background='green')

# Result
result_text = tk.StringVar()
result = tk.Label(win, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

# Cards frame
card_frame = tk.Frame(win, relief='sunken', borderwidth=1, background='green')
card_frame.grid(row=1, column=0, sticky='ew', columnspan=3, rowspan=2)

# Dealer
dealer_score_label = tk.IntVar()
tk.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tk.Label(card_frame, textvariable=dealer_score_label, background="green", fg='white').grid(row=1, column=0)

# embedded frame to hold card images
dealer_card_frame = tk.Frame(card_frame, background='green')
dealer_card_frame.grid(row=0, column=1, sticky='ew', rowspan=2)

# Player(s)
player_score_label = tk.IntVar()
#player_score = 0
#player_ace = False

tk.Label(card_frame, text='Player', background='green', fg='white').grid(row=2, column=0)
tk.Label(card_frame, textvariable=player_score_label, background='green', fg='white').grid(row=3, column=0)
player_card_frame = tk.Frame(card_frame, background='green')
player_card_frame.grid(row=2, column=1, sticky='ew', rowspan=2)

# Buttons
button_frame = tk.Frame(win)
button_frame.grid(row=3, column=0, columnspan=3, sticky='w')

dealer_button = tk.Button(button_frame, text='Dealer', command=deal_dealer) # command=fnc | not fnc() & not args
dealer_button.grid(row=0, column=0)

player_button = tk.Button(button_frame, text='Player', command=deal_player)
player_button.grid(row=0, column=1)

newgame_button = tk.Button(button_frame, text='New Game', command=new_game) # command=new_game
newgame_button.grid(row=0, column=2)

shuffle_botton = tk.Button(button_frame, text='Shuffle', command=shuffle)
shuffle_botton.grid(row=0, column=3)

# load cards
cards = []
load_images(cards)
#print(cards)


# Create a new deck of cards and shuffle them
# if you want multiple decks ...
# call load_images again and again
# deck = list(cards) + list(cards) + list(cards)
deck = list(cards)
#random.shuffle(deck)
shuffle()

# Create the list to store the dealer's and player's hands
dealer_hand = []
player_hand = []

new_game()

win.mainloop()

