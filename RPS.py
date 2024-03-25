import random
def player(prev_play,
           opponent_history=[],
            play_order=[{                     
                "RR": 0,
                "RP": 0,
                "RS": 0,
                "PR": 0,
                "PP": 0,
                "PS": 0,
                "SR": 0,
                "SP": 0,
                "SS": 0,
                }]
            ):

    def win_quincy(opponent_history): # to win Quincy
        response = {'S': 'P', 'R': 'P', 'P': 'S'}
        guess = response[opponent_history[-1]]
        if opponent_history[-2] == "R":
            guess = "S" 
        return guess
    
    def win_kris_mrugesh(): # to win Kris and Mrugesh
        response = {'S': 'P', 'R': 'S', 'P': 'R'}
        return response[player.play[-1]]
    
    def win_abbey(play_order):  # to win Abbey
        potential_plays = [
            player.play[-1] + "R",
            player.play[-1] + "P",
            player.play[-1] + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }

        abbey_prediction = max(sub_order, key=sub_order.get)[-1:]

        response = {'P': 'R', 'R': 'S', 'S': 'P'}
        return response[abbey_prediction]
    
    
    opponent_history.append(prev_play)
    last_index = len(opponent_history)-1
    if len(prev_play)==0:
        if last_index > 0:
            player.play.pop()
        player.play.append(prev_play)
        player.counter = 0
        for i in ["RR", "RP", "RS", "PR", "PP", "PS", "SR", "SP", "SS"]:
            play_order[0][i]=0

    
    last_two = "".join(player.play[-2:])
    if len(last_two) == 2:   
        play_order[0][last_two] += 1


    guess = random.choice(['R', 'P', 'S'])
    


    if player.counter > 11:
        guess = win_abbey(play_order) 
        
        window_player = player.play[last_index-10:last_index]
        most_frequent = max(set(window_player), key=window_player.count) 
        mrugesh_mapping = {'P': 'S', 'R': 'P', 'S': 'R'}
        ideal_mrugesh_response = mrugesh_mapping[most_frequent]
        if (opponent_history[-1] == ideal_mrugesh_response): # opponent is probably Mrugesh or Kris
            guess = win_kris_mrugesh()


        window_opponent = opponent_history[-10:]
        countS = window_opponent.count("S")
        countR = window_opponent.count("R")
        if (countS == 2 and countR == 4): # opponent is probably Quincy
            guess = win_quincy(opponent_history)   

        window_player = player.play[last_index-9:last_index]
        kris_mapping = {'P': 'S', 'R': 'P', 'S': 'R'}
        ideal_kris_response = []
        for i in range(9):
            ideal_kris_response.append(kris_mapping[window_player[i]])
        if (opponent_history[-9:] == ideal_kris_response): # opponent is probably Kris
            guess = win_kris_mrugesh()
  
    
    player.play.append(guess)
    player.counter += 1        

    return guess
    
player.counter = 0
player.play = [] 
