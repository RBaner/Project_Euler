hands = {1: "High Card", 2: "One Pair", 3:"Two Pair",4:"Three of a kind", 5:"Straight",6:"Flush",7:"Full House",8:"Four of a kind",9:"Straight Flush",10:"Royal Flush"}
order = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def getGames():
    with open("p054_poker.txt","r") as file:
        contents = file.readlines()
    for line in range(len(contents)):
        if '\n' in contents[line]:
            contents[line] = contents[line].replace('\n','').split(' ')
        else:
            contents[line] = contents[line].split(' ')
    return(contents)

def getHand(cards: list) -> tuple:
    # output is tuple (hand value,highest card used in hand pattern)
    # in order to differentiate similar hands (e.g. pair of queens outvalues pair of 2s even if pair of 2s has high card outside of pair)
    # certain hands (5-card hand patterns for example) dont require this metric and can rely on basic getHighestCard()
    suits = [i[1] for i in cards]
    ranks = [i[0] for i in cards]
    # Common metrics
    counts = {i:ranks.count(i) for i in order.keys()}
    all_same_suit = all([i==suits[0] for i in suits])
    if (sorted(ranks) == ['A','J','K','Q','T'] and all_same_suit):
        return((10,getHighestCard(cards))) # Royal Flush
    elif max([order[i] for i in ranks]) - min([order[i] for i in ranks]) == 4 and sorted(ranks) in [sorted(list(order.keys())[i:i+5]) for i in range(14-5)]:
        if all_same_suit:
            return((9,getHighestCard(cards))) # Straight Flush
        else:
            return((5,getHighestCard(cards))) # Straight
    elif any([ranks.count(i) == 4 for i in order.keys()]):
        return((8,order[max([i for i,v in counts.items() if v==4],key=order.get)])) # Four of a Kind
    elif any([ranks.count(i) == 3 for i in order.keys()]) and any([ranks.count(i) == 2 for i in order.keys()]):
        return((7,order[max([i for i,v in counts.items() if v==3],key=order.get)])) # Full house
    elif all_same_suit:
        return((6,getHighestCard(cards))) # Flush
    elif any([ranks.count(i) == 3 for i in order.keys()]):
        return((4,order[max([i for i,v in counts.items() if v==3],key=order.get)])) # Three of a kind
    elif any([ranks.count(i) == 2 for i in order.keys()]):
        if len([i for i in counts if counts[i]==2]) == 2:
            return((3,order[max([i for i,v in counts.items() if v==2],key=order.get)])) # Two Pair
        else:
            return((2,order[max([i for i,v in counts.items() if v==2],key=order.get)])) # One Pair
    else:
        return((1,getHighestCard(cards))) # High Card

def getHighestCard(cards: list) -> int:
    return(max([order[i] for i in [i[0] for i in cards]]))

def p54(debug=True):
    games = getGames()
    p1Tally = 0
    p2Tally = 0
    for game in games:
        player1 = getHand(game[:5])
        player2 = getHand(game[5:])
        if debug:
            print("++++++++++++++++")
            print(f"Player 1's hand: {game[:5]}") 
            print(f"Player 2's hand: {game[5:]}") 
            print(f"Player 1's score: {hands[player1[0]]}") 
            print(f"Player 2's score: {hands[player2[0]]}")
        # determine highest hand
        if player1[0] > player2[0]:
            if debug:
                print("Player 1 wins") 
            p1Tally += 1
        elif player2[0] > player1[0]:
            if debug:
                print("Player 2 wins") 
            p2Tally += 1
        # if hand patterns are equal determine highest card in pattern
        elif player1[1] > player2[1]:
            if debug:
                print("Player 1 wins") 
            p1Tally += 1
        elif player2[1] > player1[1]:
            if debug:
                print("Player 2 wins") 
            p2Tally += 1
        # if hand patterns are identical (e.g. both are pair of 2s) determine highest card in hand
        else:
            player1 = getHighestCard(game[:5])
            player2 = getHighestCard(game[5:])
            if player1 > player2:
                if debug:
                    print("Player 1 wins by high card") 
                p1Tally += 1
            elif player2 > player1:
                if debug:
                    print("Player 2 wins by high card")
                p2Tally += 1
            else:
                # This situation shouldn't happen based on problem statement
                raise Exception("Identical Hand")
    return(p1Tally)
        
def main()->int:
    return(p54())

if __name__=="__main__":
    from time import time
    start = time()
    print(main())
    end = time()
    print(end-start)