import sys

EMPTY_SPACE = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ('1', '2', '3', '4', '5', '6', '7')
assert len(COLUMN_LABELS) == BOARD_WIDTH


class FourInARow:
    def __init__(self):
        self.game_board = self.get_new_board()
        self.player_turn = PLAYER_X

    def run(self):
        print("""
        Four in a Row

        Two players take turns dropping tiles into one of seven columns, trying
        to make four in a row horizontally, vertically, or diagonally.
        """)

        while True:
            self.display_board(self.game_board)
            player_move = self.ask_for_player_move(
                self.player_turn, self.game_board)
            self.game_board[player_move] = self.player_turn

            if self.is_winner(self.player_turn, self.game_board):
                self.display_board(self.game_board)
                print(f'Player {self.player_turn} has won!')
                sys.exit()
            elif self.is_full(self.game_board):
                self.display_board(self.game_board)
                print('There is a tie!')
                sys.exit()

            self.player_turn = PLAYER_O if self.player_turn == PLAYER_X else PLAYER_X

    @staticmethod
    def get_new_board():
        return {(column_index, row_index): EMPTY_SPACE for column_index in range(BOARD_WIDTH)
                for row_index in range(BOARD_HEIGHT)}

    @staticmethod
    def display_board(board):
        tile_chars = [board[(col_idx, row_idx)] for row_idx in range(BOARD_HEIGHT)
                      for col_idx in range(BOARD_WIDTH)]
        print(f"""
         1234567
        +-------+
        |{''.join(tile_chars[0:7])}|
        |{''.join(tile_chars[7:14])}|
        |{''.join(tile_chars[14:21])}|
        |{''.join(tile_chars[21:28])}|
        |{''.join(tile_chars[28:35])}|
        |{''.join(tile_chars[35:42])}|
        +-------+""")

    @staticmethod
    def ask_for_player_move(player_tile, board):
        while True:
            response = input(
                f'Player {player_tile}, enter a column or QUIT:').upper().strip()

            if response == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if response not in COLUMN_LABELS:
                print(f'Enter a number from 1 to {BOARD_WIDTH}.')
                continue

            column_index = int(response) - 1
            if board[(column_index, 0)] != EMPTY_SPACE:
                print('That column is full, select another one.')
                continue

            for row_index in range(BOARD_HEIGHT - 1, -1, -1):
                if board[(column_index, row_index)] == EMPTY_SPACE:
                    return column_index, row_index

    @staticmethod
    def is_full(board):
        return all(
            board[(col_idx, row_idx)] != EMPTY_SPACE for row_idx in range(
                BOARD_HEIGHT) for col_idx in range(BOARD_WIDTH))

    @staticmethod
    def is_winner(player_tile, board):
        for col_idx in range(BOARD_WIDTH - 3):
            for row_idx in range(BOARD_HEIGHT):
                if all(board[(col_idx + k, row_idx)] == player_tile for k in range(4)):
                    return True

        for col_idx in range(BOARD_WIDTH):
            for row_idx in range(BOARD_HEIGHT - 3):
                if all(board[(col_idx, row_idx + k)] == player_tile for k in range(4)):
                    return True

        for col_idx in range(BOARD_WIDTH - 3):
            for row_idx in range(BOARD_HEIGHT - 3):
                if all(board[(col_idx + k, row_idx + k)] == player_tile for k in range(4)):
                    return True

                if all(board[(col_idx + 3 - k, row_idx + k)] == player_tile for k in range(4)):
                    return True

        return False


if __name__ == '__main__':
    game = FourInARow()
    game.run()
