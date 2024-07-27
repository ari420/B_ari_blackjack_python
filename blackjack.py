import random

deck = [2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 10 , 10 , 10  , 11] * 4 
dealr_hand = []
user_hand  = []

"""pic up a card from deck randomly"""
def pic_random_card ():
    new_card = random.choice(deck)
    deck.remove(new_card)
    return new_card

"""dealer cards in his hand"""
def dealer_cards (tutal_user):
    if tutal_user <= 21:
        while sum(dealr_hand) < 17:
            dealr_hand.append(pic_random_card())
    return dealr_hand    

"""giving tow cards to each player"""
def blackjack ():
    for i in range(2):
        dealr_hand.append(pic_random_card())
        user_hand.append(pic_random_card())
    print(F"dealer hand : {dealr_hand}")
    print(F'user hand : {user_hand}')    
    
    
    """user chois to have a caed or not to have a card"""    
    continue_game = True
    while continue_game == True and sum(user_hand) <= 21:
        drowing = input('do you like to drow an other card or not  (y/n):     ')
        
        if drowing == 'y':
            user_hand.append(pic_random_card())
            
            print("dealer hand : {0}".format(dealr_hand))
            print(F'user hand : {user_hand}')
            
        else:
            continue_game = False
            
            
        """to drow card for dealer""" 
        dealer_cards(sum(user_hand))
        
        """check for the final result"""
        print(f"_________________final result________________")
        print(f"user hand {user_hand} wiht a tutal of {sum(user_hand)}")  
        print(f"dealer hand {dealr_hand} wiht a tutal of {sum(dealr_hand)}")  
        
        if sum(user_hand) > 21:
            print('dealer is win :/')
        elif sum(user_hand) < sum(dealr_hand) and sum(dealr_hand) <= 21:
            print('dealer is win :/')
        elif sum(dealr_hand) == sum(user_hand):
            print('drow')
        else:
            print('user win :)') 

    
"""game main loop"""
print('____________________________________________________________________')
print('Blackjack is a card game where the user goes against the dealer')
print("Your Goal is to draw cards to get closest to 21 points,")
print("however you don't want to go above 21 points because you will lose!")

play = False

while play == False:
    play_game = input('would you like to play some blackjack (y/n)     ')
    if play_game == 'y':
        blackjack()
        play = True
    elif play_game == 'n':
        print('_______________________________')
        print('___________bay bay_____________')
        play_game = True 
        break
    else:
        print('you can only say   y  or  n :/')    