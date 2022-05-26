
import random


class TicTacToe:

    def __init__(self):
        self.inputs = []


    def initialize_board(self):
        self.board = [[f"-"for _ in range(3)] for _ in range(3)]

        assert self.board == [["-", "-", "-",],
                              ["-", "-", "-"],
                              ["-", "-", "-"]]

    def get_starting_player(self):
        random_number = random.randint(1,2)
        if random_number == 1:
            self.player = "player"
        if random_number == 2:
            self.player = "computer"

    def next_player(self):
        if self.player == "computer":
            self.player = "player"
        else:
            self.player = "computer"


    def get_input(self):

        try:
            self.row, self.col = int(input("Input the row of your choice: ")), int(input("Input a column of your choice: "))
        except:
            print("invalid input please enter an integer")
            return False

        while max(self.row, self.col) > 3 or min(self.row, self.col) < 1:
            print(f"Input {self.row, self.col} is invalid please choose a number between 1 and 3 for each")
            self.row, self.col = int(input("Input the row of your choice: ")), int(input("Input a column of your choice: "))

        #ctrim by one because a list starts at 0
        self.row, self.col = self.row -1, self.col-1

        # check if the input was used before
        if (self.row, self.col) not in self.inputs:
            self.inputs.append((self.row, self.col))
        else:
            print(f"The input {self.row + 1, self.col + 1} is invalid because it was used before please choose another input")
            return False

        print(f"You chose {self.row + 1, self.col + 1}")
        return True

    def new_turn(self):
        print(f"Its the {self.player}'s turn")
        self.print_board()
        if self.player == "player":
            while self.get_input() == False:
                pass
        if self.player == "computer":
            while self.random_choice() == False:
                pass

    def random_choice(self):
        self.row = random.randint(0,2)
        self.col = random.randint(0,2)
        if (self.row, self.col) not in self.inputs:
            self.inputs.append((self.row, self.col))
            return True
        return False

    def players_symbol(self):
        if self.player == "player":
            return "x"
        if self.player == "computer":
            return "0"

    def set_input(self):
        self.board[self.row][self.col] = self.players_symbol()
        print(f" Row {self.row + 1} and Col {self.col + 1} for the {self.player} was set")

    def win_or_not(self):
        diagonal_list = [[(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]
        list = []
        count_rows = 0
        count_cols = 0

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == self.players_symbol():
                    list.append((i,j))
                    count_rows += 1
                if self.board[j][i] == self.players_symbol():
                    count_cols += 1

                if count_rows == 3 or count_cols ==3:
                    return True
            count_rows = 0
            count_cols = 0

        count = 0
        for i in range(len(diagonal_list)):
            for j in range(len(diagonal_list[i])):
                if diagonal_list[i][j] in list:
                    count += 1
                    if count == 3:
                        return True
            count = 0

    def print_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def start_game(self):
        self.get_starting_player()
        self.initialize_board()
        for i in range(9):
            self.new_turn()
            self.set_input()
            if self.win_or_not() == True:
                if self.player == "player":
                    print(f"Congratiulations {self.player} has Won the Game")
                else:
                    print("You lost to the computer")
                self.print_board()
                return
            self.next_player()
        self.print_board()
        print ("No one WON, you can start a new Session now")


        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tic_tac_toe=TicTacToe()
    tic_tac_toe.start_game()

