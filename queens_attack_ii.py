# From https://www.hackerrank.com/challenges/queens-attack-2/problem

from enum import Enum
from typing import List


class ChessBoard:

    def __init__(
            self,
            board_length: int,
            obstacles_amount: int,
            queen_at_row: int,
            queen_at_column: int,
            obstacles_at: List[List[int]] = []
        ) -> None:
        self.board_length = board_length
        self.obstacles_amount = obstacles_amount
        self.queen_at_row = queen_at_row
        self.queen_at_column = queen_at_column
        self.obstacles_at = {(obstacle[0], obstacle[1]): True for obstacle in obstacles_at}
        self.possible_moves = None

    def get_next_row_for_direction(self, current_count: int, direction: 'ChessBoard.DirectionOption') -> int:
        if direction == ChessBoard.DirectionOption.LEFT or direction == ChessBoard.DirectionOption.RIGHT:
            return self.queen_at_row
        elif (direction == ChessBoard.DirectionOption.UP or 
            direction == ChessBoard.DirectionOption.UPPER_RIGHT or
            direction == ChessBoard.DirectionOption.UPPER_LEFT):
            return self.queen_at_row + current_count + 1
        elif (direction == ChessBoard.DirectionOption.DOWN or
            direction == ChessBoard.DirectionOption.LOWER_LEFT or
            direction == ChessBoard.DirectionOption.LOWER_RIGHT):
            return self.queen_at_row - current_count - 1
        else:
            raise ValueError('Invalid value for direction parameter')

    def get_next_column_for_direction(self, current_count: int, direction: 'ChessBoard.DirectionOption') -> int:
        if direction == ChessBoard.DirectionOption.UP or direction == ChessBoard.DirectionOption.DOWN:
            return self.queen_at_column
        elif (direction == ChessBoard.DirectionOption.LEFT or
            direction == ChessBoard.DirectionOption.UPPER_LEFT or
            direction == ChessBoard.DirectionOption.LOWER_LEFT):
            return self.queen_at_column - current_count - 1
        elif (direction == ChessBoard.DirectionOption.RIGHT or
            direction == ChessBoard.DirectionOption.UPPER_RIGHT or
            direction == ChessBoard.DirectionOption.LOWER_RIGHT):
            return self.queen_at_column + current_count + 1
        else:
            raise ValueError('Invalid value for direction parameter')

    def get_count_for_direction(self, direction: 'ChessBoard.DirectionOption') -> int:
        remaining_up = self.board_length - self.queen_at_row
        remaining_down = self.queen_at_row - 1
        remaining_left = self.queen_at_column - 1
        remaining_right = self.board_length - self.queen_at_column
        if direction == ChessBoard.DirectionOption.UP:
            return remaining_up
        if direction == ChessBoard.DirectionOption.DOWN:
            return remaining_down
        if direction == ChessBoard.DirectionOption.LEFT:
            return remaining_left
        if direction == ChessBoard.DirectionOption.RIGHT:
            return remaining_right
        if direction == ChessBoard.DirectionOption.UPPER_LEFT:
            return remaining_left if remaining_left < remaining_up else remaining_up
        if direction == ChessBoard.DirectionOption.UPPER_RIGHT:
            return remaining_right if remaining_right < remaining_up else remaining_up
        if direction == ChessBoard.DirectionOption.LOWER_LEFT:
            return remaining_left if remaining_left < remaining_down else remaining_down
        if direction == ChessBoard.DirectionOption.LOWER_RIGHT:
            return remaining_right if remaining_right < remaining_down else remaining_down
    
    class DirectionOption(Enum):
        UP = 'Up'
        DOWN = 'Down'
        LEFT = 'Left'
        RIGHT = 'Right'
        UPPER_RIGHT = 'Upper Right'
        LOWER_RIGHT = 'Lower Right'
        UPPER_LEFT = 'Upper Left'
        LOWER_LEFT = 'Lower Left'
    
    def __count_towards(self, direction: 'ChessBoard.DirectionOption') -> None:
        count_for_direction = self.get_count_for_direction(direction)
        for x in range(count_for_direction):
            if self.obstacles_amount > 0 and self.obstacles_at.get((
                self.get_next_row_for_direction(x, direction),
                self.get_next_column_for_direction(x, direction)
            )):
                self.obstacles_amount += 1
                break
            self.possible_moves += 1

    def count_queen_posible_moves(self) -> None:
        self.possible_moves = 0
        self.__count_towards(ChessBoard.DirectionOption.UP)
        self.__count_towards(ChessBoard.DirectionOption.DOWN)
        self.__count_towards(ChessBoard.DirectionOption.LEFT)
        self.__count_towards(ChessBoard.DirectionOption.RIGHT)
        self.__count_towards(ChessBoard.DirectionOption.UPPER_LEFT)
        self.__count_towards(ChessBoard.DirectionOption.UPPER_RIGHT)
        self.__count_towards(ChessBoard.DirectionOption.LOWER_LEFT)
        self.__count_towards(ChessBoard.DirectionOption.LOWER_RIGHT)


def queens_attack(n: int, k: int, r_q: int, c_q: int, obstacles: List[List[int]] = []):
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
    return chess_board.possible_moves


assert queens_attack(4, 0, 4, 4) == 9
assert queens_attack(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]]) == 10
