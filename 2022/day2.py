def get_move(letter):
    if letter in ["A", "X"]:
        move = "rock"
        move_points = 1
    elif letter in ["B", "Y"]:
        move = "paper"
        move_points = 2
    elif letter in ["C", "Z"]:
        move = "scissors"
        move_points = 3
    return {"move": move, "move_points": move_points}


def get_points(player1_move, player2_move):
    if player1_move == player2_move:
        points = (3, 3)
    elif player1_move == "rock" and player2_move == "paper":
        points = (0, 6)
    elif player1_move == "rock" and player2_move == "scissors":
        points = (6, 0)
    elif player1_move == "paper" and player2_move == "rock":
        points = (6, 0)
    elif player1_move == "paper" and player2_move == "scissors":
        points = (0, 6)
    elif player1_move == "scissors" and player2_move == "paper":
        points = (6, 0)
    elif player1_move == "scissors" and player2_move == "rock":
        points = (0, 6)
    return points


def calculate_move(player1_move, outcome):
    # X: lose, Y: draw, Z: win
    if outcome == "Y":
        player2_move = player1_move
    elif player1_move == "rock" and outcome == "Z":
        player2_move = "paper"
    elif player1_move == "rock" and outcome == "X":
        player2_move = "scissors"
    elif player1_move == "paper" and outcome == "X":
        player2_move = "rock"
    elif player1_move == "paper" and outcome == "Z":
        player2_move = "scissors"
    elif player1_move == "scissors" and outcome == "X":
        player2_move = "paper"
    elif player1_move == "scissors" and outcome == "Z":
        player2_move = "rock"
    return player2_move


def get_move_points(move):
    if move == "rock":
        move_points = 1
    elif move == "paper":
        move_points = 2
    elif move == "scissors":
        move_points = 3
    return move_points


with open("input/day2.txt", "r") as f:
    player2_points = 0
    for t in f.readlines():
        moves = list(map(get_move, t.split()))
        round_points = get_points(moves[0]["move"], moves[1]["move"])
        move_points = [t["move_points"] for t in moves]
        player2_points += (round_points[1] + move_points[1])

    print(f"oppgave 1: {player2_points}")

with open("input/day2.txt", "r") as f:
    player2_points = 0
    for t in f.readlines():
        player1_move = get_move(t.split()[0])["move"]
        player2_move = calculate_move(player1_move, t.split()[1])
        round_points = get_points(player1_move, player2_move)
        move_points = get_move_points(player2_move)
        player2_points += (round_points[1] + move_points)

    print(f"oppgave 2: {player2_points}")
