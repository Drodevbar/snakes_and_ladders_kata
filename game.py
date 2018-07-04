class SnakesLadders:
    __movable_squares: dict = {
        2: 38, 7: 14, 8: 31,
        15: 26, 21: 42, 28: 84, 36: 44,
        51: 67, 71: 91, 78: 98, 87: 94,
        16: 6, 46: 25, 49: 11, 62: 19, 64: 60,
        74: 53, 89: 68, 92: 88, 95: 75, 99: 80
    }

    def __init__(self):
        self.__game_over: bool = False
        self.__current_player: int = 1
        self.__player_squares: dict = {
            1: 0,
            2: 0
        }

    def play(self, die1: int, die2: int) -> str:
        square_sum: int = self.__player_squares[self.__current_player] + die1 + die2

        if self.__game_over:
            return "Game over!"
        if square_sum == 100:
            self.__game_over = True
            return "Player {0} Wins!".format(self.__current_player)
        if square_sum > 100:
            square_sum = 200 - square_sum

        self.__player_squares[self.__current_player] = self.__next_square(square_sum)

        response: str = "Player {0} is on square {1}".format(
            self.__current_player, self.__player_squares[self.__current_player]
        )
        self.__swap_players(die1, die2)

        return response

    def __next_square(self, square_sum: int) -> int:
        return self.__movable_squares.get(
            square_sum,
            square_sum
        )

    def __swap_players(self, die1: int, die2: int) -> None:
        if not die1 == die2:
            self.__current_player = 2 if self.__current_player == 1 else 1
