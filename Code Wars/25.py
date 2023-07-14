'''
Rock Paper Scissors
Let's play! You have to return which player won! In case of a draw return Draw!.

Examples(Input1, Input2 --> Output):

"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"


'''

# def rps(p1, p2):
#     #your code here
#     if p1 == p2:
#         return 'Draw!'
#     elif p2 == 'scissors' and p1 =='paper':
#         return "Player 2 won!"
#     elif p2 == 'paper' and p1 =='scissors':
#         return "Player 1 won!"
#     elif p2 == 'paper' and p1 =='rock':
#         return "Player 2 won!"
#     elif p2 == 'rock' and p1 =='paper':
#         return "Player 1 won!"
#     elif p2 == 'rock' and p1 =='scissors':
#         return "Player 2 won!"
#     elif p2 == 'scissors' and p1 =='rock':
#         return "Player 1 won!"

#another code

RPS = {('rock', 'rock'): 'Draw!',
       ('rock', 'paper'): 'Player 2 won!',
       ('rock', 'scissors'): 'Player 1 won!',
       ('paper', 'rock'): 'Player 1 won!',
       ('paper', 'paper'): 'Draw!',
       ('paper', 'scissors'): 'Player 2 won!',
       ('scissors', 'rock'): 'Player 2 won!',
       ('scissors', 'paper'): 'Player 1 won!',
       ('scissors', 'scissors'): 'Draw!'}


def rps(p1, p2):
    return RPS[(p1, p2)]