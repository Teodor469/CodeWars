def rps(p1, p2):
    l = ['rock', 'paper', 'scissors']

    if p1 == l[0] and p2 == l[1]:
        return 'Player 2 won!'
    elif p1 == l[1] and p2 == l[2]:
        return 'Player 2 won!'
    elif p1 == l[2] and p2 == l[0]:
        return 'Player 2 won!'
    elif p1 == p2:
        return 'Draw!'
    else:
        return 'Player 1 won!'
    

#found this on the app IT'S BEAUTIFUL 
# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]]