# From https://www.hackerrank.com/challenges/queens-attack-2/problem

from typing import List


class ChessBoard:

    def __init__(
            self,
            board_length: int,
            obstacles_amount: int,
            queen_at_row: int,
            queen_at_column: int,
            obstacles_at: List[List[int]]
        ) -> None:
        self.board_length = board_length
        self.queen_at_row = queen_at_row
        self.queen_at_column = queen_at_column
        self.obstacles_at = obstacles_at
        self.possible_moves = None
    
    def __count_upwards(self) -> None:
        for x in range(self.board_length - self.queen_at_row):
            if self.__is_square_blocked(
                row = self.queen_at_row + x + 1,
                column = self.queen_at_column
            ):
                break
            self.possible_moves += 1

    def __count_downwards(self) -> None:
        for x in range(self.queen_at_row):
            if x + 1 == self.queen_at_row or self.__is_square_blocked(
                row = self.queen_at_row - x - 1,
                column = self.queen_at_column
            ):
                break
            self.possible_moves += 1

    def __count_towards_left(self) -> None:
        for x in range(self.queen_at_column):
            if x + 1 == self.queen_at_column or self.__is_square_blocked(
                row = self.queen_at_row,
                column = self.queen_at_column - x - 1
            ):
                break
            self.possible_moves += 1
    
    def __count_towards_right(self) -> None:
        for x in range(self.board_length - self.queen_at_column):
            if self.__is_square_blocked(
                row = self.queen_at_row,
                column = self.queen_at_column + x + 1
            ):
                break
            self.possible_moves += 1
    
    def __count_upper_left_diagonal(self) -> None:
        remaining_up = self.board_length - self.queen_at_row
        smaller = remaining_up if remaining_up < self.queen_at_column else self.queen_at_column
        for x in range(smaller):
            if self.__is_square_blocked(
                row = self.queen_at_row + x + 1,
                column = self.queen_at_column - x - 1
            ):
                break
            self.possible_moves += 1

    def __count_upper_right_diagonal(self) -> None:
        remaining_up = self.board_length - self.queen_at_row
        remaining_right = self.board_length - self.queen_at_column
        smaller = remaining_right if remaining_right < remaining_up else remaining_up
        for x in range(smaller):
            if self.__is_square_blocked(
                row = self.queen_at_row + x + 1,
                column = self.queen_at_column + x + 1
            ):
                break
            self.possible_moves += 1

    def __count_lower_right_diagonal(self) -> None:
        remaining_down = self.queen_at_row
        remaining_right = self.board_length - self.queen_at_column
        smaller = remaining_right if remaining_right < remaining_down else remaining_down
        for x in range(smaller):
            if self.__is_square_blocked(
                row = self.queen_at_row - x - 1,
                column = self.queen_at_column + x + 1
            ):
                break
            self.possible_moves += 1

    def __count_lower_left_diagonal(self) -> None:
        remaining_down = self.queen_at_row
        remaining_left = self.queen_at_column
        smaller = remaining_left if remaining_left < remaining_down else remaining_down
        for x in range(smaller):
            if self.__is_square_blocked(
                row = self.queen_at_row - x - 1,
                column = self.queen_at_column - x - 1
            ):
                break
            self.possible_moves += 1

    def __is_square_blocked(self, row: int, column: int) -> bool:
        if not self.obstacles_at:
            return False
        for obstacle in self.obstacles_at:
            if obstacle[0] == row and obstacle[1] == column:
                self.obstacles_at.remove(obstacle)
                return True
        return False

    def count_queen_posible_moves(self) -> None:
        self.possible_moves = 0
        self.__count_upwards()
        self.__count_downwards()
        self.__count_towards_left()
        self.__count_towards_right()
        self.__count_upper_left_diagonal()
        self.__count_upper_right_diagonal()
        self.__count_lower_right_diagonal()
        self.__count_lower_left_diagonal()


def queens_attack(n: int, k: int, r_q: int, c_q: int, obstacles: List[List[int]]):
    """Resolve queens attack.

    Parameters
    ----------

    int n: the number of rows and columns in the board.

    int k: the number of obstacles on the board.

    int r_q: the row number of the queen's position.

    int c_q: the column number of the queen's position.

    int obstacles[k][2]: each element is an array of integers, the row and
        column of an obstacle.

    Return
    ------

    int: the number of squares the queen can attack
    """
    chess_board = ChessBoard(n, k, r_q, c_q, obstacles)
    chess_board.count_queen_posible_moves()
    print(chess_board.possible_moves)


queens_attack(
    5,
    3,
    4,
    3,
    [[5, 5], [4, 2], [2, 3]]
)
