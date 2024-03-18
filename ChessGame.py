class ChessBoard:
    def __init__(self):
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.current_turn = 'white'

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start_pos, end_pos):
        start_row, start_col = start_pos
        end_row, end_col = end_pos

        piece = self.board[start_row][start_col]
        if piece == ' ':
            print("No piece at the given position!")
            return False

        if self.current_turn == 'white' and piece.islower():
            print("It's black's turn!")
            return False
        elif self.current_turn == 'black' and piece.isupper():
            print("It's white's turn!")
            return False

        # Check if move is valid (basic checks, doesn't handle check/checkmate)
        if self.board[end_row][end_col] != ' ':
            print("Invalid move! There's a piece at the destination.")
            return False

        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = ' '

        self.current_turn = 'white' if self.current_turn == 'black' else 'black'
        return True

if __name__ == "__main__":
    board = ChessBoard()

    while True:
        board.print_board()
        start_pos = input("Enter start position (row col): ").split()
        start_pos = tuple(map(int, start_pos))
        end_pos = input("Enter end position (row col): ").split()
        end_pos = tuple(map(int, end_pos))

        if not board.move_piece(start_pos, end_pos):
            print("Invalid move! Try again.")
        else:
            print(f"{board.current_turn.capitalize()}'s turn")