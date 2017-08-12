import handler
from deck import Deck
from player import Player
from functools import reduce


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

nums_dist = {1:6, 2:5, 3:5, 4:4, 
    5:4, 6:4, 7:4, 8:4, 9:4
}

ops_dist = {
    '+': 10,
    '-': 10,
    'x': 10,
    '/': 10,
}


def prep_players():
    player1 = Player("joe", build_op_deck().shuffle(), build_num_deck().shuffle())
    player2 = Player("john", build_op_deck().shuffle(), build_num_deck().shuffle())



    player1.draw_card(player1.op_deck, player1.op_hand, 5)
    player1.draw_card(player1.num_deck, player1.num_hand, 5)

    player2.draw_card(player2.op_deck, player2.op_hand, 5)
    player2.draw_card(player2.num_deck, player2.num_hand, 5)
    return player1, player2    

def build_op_deck():
    return Deck(reduce(lambda x, y: x + y, list(map(lambda x : [x] * ops_dist[x], 
                                                    list(ops_dist.keys())
                                                    ))))

def build_num_deck():
    return Deck(reduce(lambda x,y: x + y, list(map(lambda x: [x] * nums_dist[x],
                                                   [i for i in range(1,10)]))))

def colorize(thing, color = None):
    if color == None:
        return thing
    if color == "green":
        return bcolors.OKGREEN + str(thing) + bcolors.ENDC
    if color == "yellow":
        return bcolors.WARNING + str(thing) + bcolors.ENDC
    if color == "red":
        return bcolors.FAIL + str(thing) + bcolors.ENDC
    if color == "blue":
        return bcolors.OKBLUE + str(thing) + bcolors.ENDC
    if color == "purple":
        return bcolors.HEADER + str(thing) + bcolors.ENDC
    if color == "underline":
        return bcolors.UNDERLINE + str(thing) + bcolors.ENDC

def present_op_hand(player):
    hand = player.op_hand
    return colorize(" ".join(hand), color = "green")


def present_num_hand(player):
    hand = list(map(str, player.num_hand))

    return colorize(" ".join(hand), color = "blue")

def prompt_player(player):
    print(colorize(" " * 20, color = "underline"))
    print(colorize("Health: " + str(player.hp), color = "red"))
    print(colorize("Opdeck cards: " + str(len(player.op_deck.cards)) + ", Numdeck cards: " + str(len(player.num_deck.cards)), color = "red"))
    print(colorize(" " * 20, color = "underline"))
    print(colorize("Operation hand:", color = "yellow"))
    print(present_op_hand(player))
    print(colorize("Number hand:", color = "yellow"))
    print(present_num_hand(player))
    print(colorize(" " * 20, color = "underline"))

pl1, pl2 = prep_players()
players = [pl1, pl2]
curr = 0
while True:
    pl = players[curr]
    pl.draw_card(pl.op_deck, pl.op_hand)
    pl.draw_card(pl.num_deck, pl.num_hand)


    prompt_player(pl)
    
    pl_input = input()
    pl_input = list(map(int, pl_input.split(" ")))
    pl_input[-1] = players[(curr + pl_input[-1])%2]

    
    turn_params = pl.activate_card(*pl_input)
    handler.execute_move(*turn_params)

    curr = (curr + 1)%2


