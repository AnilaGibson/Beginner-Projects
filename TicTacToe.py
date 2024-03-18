class TicTacToe:
    def __init__(self):
        self.board = ["-" for _ in range(9)]
        self.game_still_going = True
        self.winner = None
        self.current_player = "X"

    def display_board(self):
        print("\n")
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + "     1 | 2 | 3")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5] + "     4 | 5 | 6")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8] + "     7 | 8 | 9")
        print("\n")

    def handle_turn(self):
        print(self.current_player + "'s turn.")
        position = input("Choose a position from 1-9: ")

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"] or self.board[int(position) - 1] != "-":
            position = input("Invalid input. Choose an empty position from 1-9: ")

        position = int(position) - 1
        self.board[position] = self.current_player
        self.display_board()

    def check_if_game_over(self):
        self.check_for_winner()
        self.check_for_tie()

    def check_for_winner(self):
        winning_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]

        for condition in winning_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != "-":
                self.game_still_going = False
                self.winner = self.board[condition[0]]
                return

    def check_for_tie(self):
        if "-" not in self.board:
            self.game_still_going = False

    def flip_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        while self.game_still_going:
            self.display_board()
            self.handle_turn()
            self.check_if_game_over()
            self.flip_player()

        if self.winner:
            print(self.winner + " won.")
        else:
            print("It's a tie.")


if __name__ == "__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.play_game()
