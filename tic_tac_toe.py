gameboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
available_numbers = [x for x in range(1, 10)]
status = 'in progress'
last_player = 'O'


def print_gameboard():
    for row in gameboard:
        print('|', row[0], '|', row[1], '|', row[2], '|')


while status == 'in progress':
    print_gameboard()

    #  1. select player 'X' or 'O'
    if last_player == 'O':
        current_player = 'X'
    else:
        current_player = 'O'

    #  2. get and validate palyer's input
    while True:
        player_input = input(f"\n'{current_player}' player, please enter "
                             f"an available number: ")
        try:
            player_input = int(player_input)
        except ValueError:
            print_gameboard()
            print(f"\n'{player_input}' is not a number.")
            continue
        else:
            if player_input not in available_numbers:
                print_gameboard()
                print(f"\n{player_input} is out of range.")
                continue
            else:
                break

    #  3. make a game move
    for r in gameboard:
        for v in r:
            if v == player_input:
                gameboard[gameboard.index(r)][r.index(v)] = current_player
                available_numbers.remove(player_input)
    print_gameboard()

    #  4. check game status
    win = [current_player]*3
    if ([gameboard[0][0], gameboard[0][1], gameboard[0][2]] == win or
        [gameboard[1][0], gameboard[1][1], gameboard[1][2]] == win or
        [gameboard[2][0], gameboard[2][1], gameboard[2][2]] == win or
        [gameboard[0][0], gameboard[1][0], gameboard[2][0]] == win or
        [gameboard[0][1], gameboard[1][1], gameboard[2][1]] == win or
        [gameboard[0][2], gameboard[1][2], gameboard[2][2]] == win or
        [gameboard[0][0], gameboard[1][1], gameboard[2][2]] == win or
        [gameboard[0][2], gameboard[1][1], gameboard[2][0]] == win):
        status = 'finish'
        print(f"\n'{current_player}' player won!")
    elif len(available_numbers) == 0:
        status = 'finish'
        print(f'\nDraw!')
    else:
        last_player = current_player
