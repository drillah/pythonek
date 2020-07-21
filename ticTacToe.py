# kółko i krzyżyk
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Wyświetl instrukcję gry."""
    print(
        """
        Witaj w największym intelektualnym wyzwaniu wszech czasów, jakim jest gra
        'Kółko i Krzyżyk'. Będzie to ostateczna rozgrywka między Twoim ludzkim
        mózgiem a moim krzemowym procesorem.

        Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8,
        liczba ta odpowiada pzoycji a planszy zgodnie z poniższym schematem:

                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

        Przygotuj się, Człowieku. Ostateczna batalia niebawem się rozpocznie. \n
        """)

def ask_yes_no(question):
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, hight):
    response = None
    while response not in range(low, hight):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nWięc pierwszy ruch należy do Ciebie. Bedzie Ci potrzebny.")
        human = X
        computer = O
    else:
        print("\nTwoja odwaga Cię zgubi...Ja wykonam pierwszy ruch.")
        computer = X
        human = O
    return computer, human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]

    if EMPTY not in board:
        return TIE
    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Jaki będzie Twój ruch? (0 - 8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTo pole jest już zajęte, niemądry Człowieku. Wybierz inne.\n")
    print("Znakomicie...")
    return move

def computer_move(board, computer, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Wybieram pole numer", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#Kontynuować na stronie 195