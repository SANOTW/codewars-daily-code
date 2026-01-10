def rps(p1, p2):
    #your code here
    if p1 == p2:
        return "Draw!"
    
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }
    
    if wins[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"
