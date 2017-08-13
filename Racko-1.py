'''This is a code for a game knwown as racko. Racko is a game that involves rearranging
your hand of cards in order to have an increasing sequence.The user’s moves are decided by the user by asking for input,
the computer’s moves are decided by  the programmer'''

import random


def shuffle(cardstack):
    random.shuffle(cardstack) #Shuffles a deck of cards to start the game

def check_racko(rack):
    '''Check if the game has been won by achieving Racko'''
    deck=rack[:]#makes a copy of the rack
    deck.sort()#sorts the deck
    if rack==deck: #compares the deck to its sorted duplicate to see if Racko has been achieved
        return True       
    else:
        return False
    
def get_top_card(card_stack):
    return card_stack[0] #get the top card from any stack of cards.

def deal_initial_hands(deck):
    '''start the game off by dealing two hands of 10 cards each'''
    user=[]#Initializes the user's hand
    computer=[]#initializes the computer's hand
    for i in range(10):     
        computer.append(deck[i])# Adds to the computer's hand
        deck.pop(i)#Removes the value added to the computer's hand from the deck
        user.append(deck[i+1])# Adds to the user's hand
        deck.pop(i+1)#Removes the value added to the user's hand from the deck
    return (computer, user)
def print_top_to_bottom(rack):
    for i in range(len(rack)):#print it out from top to bottom
        print rack[i]
    
def find_and_replace(new_card, card_to_be_replaced, hand, discard):
    '''find the card
    to be replaced (represented by a number) in the hand and replace it with newCard.
    The replaced card then gets put on top of the discard.'''
    
    if card_to_be_replaced not in hand: # Ensure that the value entered is always in hand
        print "Error! Card to be replaced has to be in Hand"
        return "Error"
    else:#replaces with the new card and add the old card to the discard pile
        discard.insert(0,card_to_be_replaced)
        index=hand.index(card_to_be_replaced)
        hand.remove(card_to_be_replaced)
        hand.insert(index,new_card)
        return(hand,discard)
def add_card_to_discard(card, discard):
    discard.insert(0,card)# add the replaced card to the top of the discard pile

def count(hand):
    '''Counts the  number of descending points in a list'''
    
    count=0#initializes the count
    for i in range(len(hand)-1): # loops through the whole list      
        if hand[i]>hand[i+1]:
            count+=1# increments everytime there is a drop in the value in a list
        else:
            count=count
    return count
def computer_play(hand, deck, discard_pile):
    '''Criteria the computer uses to pick cards and replace its hand. First replaces 60 and 1 at the end if
    they are available. Then loops to make sure limit each position has a range of six numbers for even distribution
    and then checking for and ascending pattern'''
 
    counter1=[]#inititializes value to be used for counting descending points
    counter2=[]
    fake_dis=[6]#hold for discard pile while looping to avoid mutating the actual discard pile
    
    if discard_pile[0]==60:#places 60 to the bottom of the pile if available from discard
        find_and_replace(discard_pile[0],hand[9],hand,discard_pile)#
        discard_pile.pop(1)
        return discard_pile[0]
    elif discard_pile[0]==0:#places 0 to the top of the pile if available from discard
        find_and_replace(discard_pile[0],hand[0],hand,discard_pile)
        discard_pile.pop(1)
        return discard_pile[0]
    elif deck[0]==60:#places 60 to the bottom of the pile if available from deck
        find_and_replace(deck[0],hand[9],hand,discard_pile)
        deck.pop(0)
        return discard_pile[0]
    elif deck[0]==0:#places 0 to the top of the pile if available from deck
        find_and_replace(deck[0],hand[0],hand,discard_pile)
        deck.pop(0)
        return discard_pile[0]
    else:
            
        for i in range(10):
            ''' Distributes the possible deck values evenly on the rack'''
            if hand[i]>(i+1)*6 or hand[i]<(i+1)*6-6:#each position gets  6 possible consecutive digits
                if discard_pile[0]<(i+1)*6 and discard_pile[0]>(i+1)*6-6:
                    find_and_replace(discard_pile[0],hand[i],hand,discard_pile)#replaces from the discard
                    discard_pile.pop(1)
                    return discard_pile[0]
                elif deck[0]<(i+1)*6 and deck[0]>(i+1)*6-6:
                    find_and_replace(deck[0],hand[i],hand,discard_pile)#replaces from the deck 
                    deck.pop(0)
                    return discard_pile[0]               
    
        for i in range(10):
            ''' Loops through or possible values and find the one with the least descending positions/
            ascends'''
            k=hand[:]#make a copy of the hand for a mock run of possible values in the for loop
            h=hand[:]
                
            prod1=find_and_replace(discard_pile[0],k[i],k,fake_dis)#replaces from the discarded pile
            p_hand1=prod1[0]
            counter1.append(count(p_hand1))#appends the number of descending point
            prod2=find_and_replace(deck[0],h[i],h,fake_dis)#replaces from the deck's top card
            p_hand2=prod2[0]
            counter2.append(count(p_hand2))#appends the number of descending point
        min2=min(counter2)#minimum ascending points
        min_ind2=counter2.index(min2)#finds the index
        min1=min(counter1)#minimum ascending points
        min_ind1=counter1.index(min1)
        current_count=count(hand)
        '''replaces a hand with a value that provides least inflections'''
        if min2<current_count and min2<=min1:
            find_and_replace(deck[0],hand[min_ind2],hand,discard_pile)
            deck.pop(0)
            return discard_pile[0]
        elif min1<current_count and min1<=min2:
            find_and_replace(discard_pile[0],hand[min_ind1],hand,discard_pile)
            discard_pile.pop(1)
            return discard_pile[0]
        else:        # if Computer chooses to Pass return the available discard value
            return discard_pile[0]
   
        
def main():
    deck=list(range(1,61))#Creates
    shuffle(deck)#shuffles the deck
    racko=False#initializes racko as False
    hands=deal_initial_hands(deck)#Hand the initial cards to both the computer and the user
    users_hand=hands[1]#assign one element of this tuple as the user’s hand
    computers_hand=hands[0]#assigns the other element as the computer's hand
    print "USERS HAND"
    print_top_to_bottom(users_hand)#print users hands
    discard_pile=[get_top_card(deck)]#provided an initial discard_pile
    deck.pop(0)#removes the card that has initiallized discard pile
    print "\n"
    print "The card on top of the discard pile is",discard_pile[0]#reveals one card to begin the discard pile
    print "\n"
    while racko==False:#while the has not been worn
        computer_move=computer_play(computers_hand, deck, discard_pile)
        racko=check_racko(computers_hand)#if the computer has achieved racko
        if racko==True:
            print "GAME OVER. The computer Won"
            break
        print "\n"
        print computer_move
        choice=raw_input( "Do you want the card above? answer=y/n")#ask the user if they want the card
        print "\n"

    
        if choice=="y":#if the user chooses the card
            kick_out=input("What card number do you want to kick out?")
            users_hand_trial=users_hand[:]#make a copy of the users hand
            while find_and_replace(computer_move,kick_out,users_hand_trial,discard_pile)=="Error":
                users_hand_trial=users_hand[:]
                kick_out=input(" Try again.What card number do you want to kick out?")
        
            find_and_replace(computer_move,kick_out,users_hand,discard_pile)#replaces the card
            discard_pile.pop(1)#removes the selected card from the discard_pile
            print_top_to_bottom(users_hand)
            print "\n"
    
        elif choice=="n":#if the user rejects the card
            card=get_top_card(deck)#get a card from the top of the deck
            deck.remove(card)#removes the card
            print card
            choice2=raw_input("Do you want the card above? answer=y/n")
            if choice2=="y":
                kick_out2=input("What card number do you want to kick out?")
                users_hand_trial=users_hand[:]
                while find_and_replace(computer_move,kick_out2,users_hand_trial,discard_pile)=="Error":
                    users_hand_trial=users_hand[:]
                    kick_out2=input(" Try again.What card number do you want to kick out?")
                find_and_replace(card,kick_out2,users_hand,discard_pile)#modifies the user's hand and discard pile
                print_top_to_bottom(users_hand)
                print"\n"
            else:
                add_card_to_discard(card,discard_pile)# rejected card is added to the discard pile
                print_top_to_bottom(users_hand)
        if len(deck)<=0:#if the deck runs out
            shuffle(discard_pile)#shuffles the discard pile
            deck=discard_pile[:]#discard_pile is assigned as the deck
            discard_pile=[get_top_card(deck)]#reassign the top deck to become discard
        racko=check_racko(users_hand)#check  if the user has achieved racko
        if racko==True:
            print"Hurrah, You Won!!!"
            break
 

if __name__ == '__main__':
    main()            
 

