# Portable Python 3.2.5.1

class Board:

    def __init__(self):
        """__init_ method"""
        self.x = "-"
        self.y = "|"
        self.z = "  "
        self.zz = ""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # the list for the board items (0-8)

    def Draw(self):
        """Draws the board without square numbers then draws the board with square numbers"""
        print('The Board looks like this: \n')  # draw the board without any square numbers
        print((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), self.z, self.y, self.z, self.y, self.z, self.y, self.z)
        print('\n')
        print('The Board with the square numbers looks like this: \n')  # draw the borad with the square numbers
        print((self.z * 16), 1, self.zz, self.y, 2, self.zz, self.y, 3, self.zz, self.y, 4)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), 5, self.zz, self.y, 6, self.zz, self.y, 7, self.zz, self.y, 8)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), 9, self.zz, self.y, 10, self.y, 11, self.y, 12)
        print((self.z * 16), self.x * 17)
        print((self.z * 16), 13, self.y, 14, self.y, 15, self.y, 16)
        print('\n')


class Mark(Board):

    def draw(self, square_number, mark):
        """Draws the borad with current values"""
        self.square_number = square_number – 1  # subtract 1 from the square number – list board starts at position 0 – (0-8)
        self.mark = mark  # mark is either "X" or "O"
        self.board[self.square_number] = self.mark  # set the position in list board to either "X" or "O"
        for i in range(16):  # loop thru the values in list board
            try:
                self.board[i] += 1  # checks if the value in list board is an integer,
                self.board[i] = " "  # if it is, set it equal to a space (" ")
            except TypeError:  # if the value is an "X" or an "O", just pass
                pass
        print('\n')
        print((self.z * 16), self.board[0], self.y, self.board[1], self.y, self.board[2], self.y,
              self.board[3])  # print the first row of the board, with current values
        print((self.z * 16), self.x * 14)
        print((self.z * 16), self.board[4], self.y, self.board[5], self.y, self.board[6], self.y,
              self.board[7])  # print the second row of the board, with current values
        print((self.z * 16), self.x * 14)
        print((self.z * 16), self.board[8], self.y, self.board[9], self.y, self.board[10], self.y,
              self.board[11])  # print the third row of the board, with the current values
        print((self.z * 16), self.x * 14)
        print((self.z * 16), self.board[12], self.y, self.board[13], self.y, self.board[14], self.y,
              self.board[15])  # print the fourth row of the board with the current values
        print('\n')


class Play(Mark):

    def select_square(self):
        """Starts the game with square selection"""
        self.switch = True  # initializes the switch for the while loop to True
        self.turn = ["X", "O"]  # turn is either an "X" or an "O"
        self.counter = 0  # set counter for a possible Tie game – (no winner)
        while self.switch == True:  # starts the while loop
            for move in range(2):  # alternate between "X" and "O"
                self.move = move
                self.get_input(self.turn, self.move)  # calls the get_input function
                if self.switch == False:  # checks to see if the while loop switch has been set to False
                    break  # if it has, break out of the while loop – end game
                else:
                    self.counter += 1  # increment the counter by 1
                if self.counter == 16:  # if 9 moves have been made with no winner
                    print("The game is a Tie – no winner.\n")  # prints message – the game is a tie
                    self.switch = False  # set while loop switch to False
                    break  # break out of the while loop
                else:
                    continue  # if counter in not equal to 9, continue alternating between "X" and "O"

    def get_input(self, turn, move):
        """Gets input from user"""
        self.turn = turn
        self.move = move
        try:
            sn = int(
                input(self.turn[self.move] + " Enter a square number (1-16) for your move: "))  # get input from user
            if self.check_input(sn) == True:  # check the input for errors, call the check_input function
                self.draw(sn, self.turn[move])  # if no errors, draw the grid, call the draw function
                if self.check_win(self.turn, move) == True:  # Check if move is a win, call the check_win function
                    self.print_win(self.turn, move)  # if win, print win message, call the print_win function
                else:
                    pass
            else:
                pass
        except ValueError:
            print("\nError: Please enter a number between 1-16\n")  # print message if a letter is entered
            self.Draw()  # Draw the board and square numbers again, calls the Draw function
            self.get_input(self.turn, self.move)  # try to get input again, call the get_input function

    def check_input(self, square_number):
        """Checks the input for errors"""
        self.square_number = square_number
        if ((self.square_number >= 1) and (self.square_number <= 16)):  # make sure number is between 1-16
            if ((self.board[self.square_number – 1]) == "X") \
                    or ((self.board[self.square_number – 1]) == "O"):  # make sure the square is not already taken
                print(
                    "\nError: That space is already taken, please choose an open space.\n")  # print message if space taken
                self.get_input(self.turn, self.move)  # try to get input again, call the get_input function
            else:
                return True  # if the number is between 1-9 and the space is not taken – return True
        else:
            print(
                "\nError: That is not a valid square number, please enter a value between 1-16\n")  # print message if number is out or range
            self.Draw()  # Draw the board and square numbers again, calls the Draw function
            self.get_input(self.turn, self.move)  # try to get input again, call the get_input function

    def check_win(self, turn, move):
        """Checks the ten possibilites for a win"""
        if (self.board[0] == self.turn[move] and self.board[1] == self.turn[move] \
                and self.board[2] == self.turn[move] and self.board[3] == self.turn[move]):
            return True
        elif (self.board[4] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[6] == self.turn[move] and self.board[7] == self.turn[move]):
            return True
        elif (self.board[8] == self.turn[move] and self.board[9] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[11] == self.turn[move]):
            return True
        elif (self.board[12] == self.turn[move] and self.board[13] == self.turn[move] \
              and self.board[14] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[4] == self.turn[move] \
              and self.board[8] == self.turn[move] and self.board[12] == self.turn[move]):
            return True
        elif (self.board[1] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[9] == self.turn[move] and self.board[13] == self.turn[move]):
            return True
        elif (self.board[2] == self.turn[move] and self.board[6] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[14] == self.turn[move]):
            return True
        elif (self.board[3] == self.turn[move] and self.board[7] == self.turn[move] \
              and self.board[11] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[0] == self.turn[move] and self.board[5] == self.turn[move] \
              and self.board[10] == self.turn[move] and self.board[15] == self.turn[move]):
            return True
        elif (self.board[3] == self.turn[move] and self.board[6] == self.turn[move] \
              and self.board[9] == self.turn[move] and self.board[12] == self.turn[move]):
            return True
        else:
            return False

    def print_win(self, turn, move):
        """Prints the winning message"""
        print(str(turn[move]) + " Wins ! \n")  # prints the winning message
        self.switch = False  # sets the looping switch in select_square function to False
        return self.switch  # returns the value of the switch (False)


b1 = Play()  # Create object b1 of the Play class – (Play class inherits from the Mark class which inherits from the Board class)
b1.Draw()  # Call the Draw function in the Board class
b1.select_square()  # Start the game by calling the select_square function in the Play class