#Welcome to Sudoku
import pygame, sys
from constants import *
from sudoku_generator import *
from sudoku import Sudoku

def main():
    gboard = Sudoku()
    gboard.start_screen()

    while True:
        # event loop
        for event in pygame.event.get():
            # quits program
            if event.type == pygame.QUIT:
                gboard.done()

            # registers both mouse click and scroll wheel
            # updates gameMode to the number of empty boxes
            # increases count by one and prints the board
            if event.type == pygame.MOUSEBUTTONUP and gboard.count == 0:
                gameMode = gboard.setGameMode(event.pos[0], event.pos[1])
                if gameMode != 0:
                    gboard.count += 1
                    pygame.time.wait(500)
                    # makes the game
                    gboard.makeSudoku(gameMode)
                    gboard.loadGameBoard()

            # checks to find the selected cell
            elif gboard.count == 1 and event.type == pygame.MOUSEBUTTONUP and event.pos[1] <= (WIDTH - (WIDTH // 10)):
                # finds the row and column the user clicked in and highlights box through the highLightBox function
                # sets cell to selected cell
                x, y = event.pos[0], event.pos[1]
                col = x // cellWidth
                row = y // cellHeight
                gboard.highLightBox(col, row)
                gboard.selectedCell = (row, col)

            # checks if the user clicked a button and deals with it accordingly
            elif gboard.count == 1 and event.type == pygame.MOUSEBUTTONUP:
                isThereAReset = gboard.checkBottomButtons(event.pos[0], event.pos[1])
                if isThereAReset:
                    gboard.reset(gboard.ogBoard)
                    gboard.loadGameBoard()

            # have on for enter and make sure that a valid box is selected, and it has a sketch value
            # checks to see if click is in the grid part of the screen
            # check after value is enter

            # checks for a key press and validity of selected cell
            elif gboard.count == 1 and event.type == pygame.KEYDOWN:
                # notes the selected cell
                row = gboard.selectedCell[0]
                col = gboard.selectedCell[1]

                # checks to make sure an empty cell is selected
                condition = gboard.sketch[row][col] != 10 and gboard.board[row][col] == 0

                # stops if no cell is selected yet
                if gboard.selectedCell[0] == -1:
                    continue

                # checks to see if user pressed enter/return and whether the cell is empty
                # sets the board value to the sketch value, sets sketch value back to 0
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    # checks if cell is empty and enlarges the value to show guess is locked
                    if condition:
                        gboard.board[row][col] = gboard.sketch[row][col]
                        gboard.sketch[row][col] = 0

                # checks to see if the selected cell is empty and sets the input to the sketch list
                elif event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    if condition:
                        gboard.sketch[row][col] = 1
                elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    if condition:
                        gboard.sketch[row][col] = 2
                elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    if condition:
                        gboard.sketch[row][col] = 3
                elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    if condition:
                        gboard.sketch[row][col] = 4
                elif event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    if condition:
                        gboard.sketch[row][col] = 5
                elif event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    if condition:
                        gboard.sketch[row][col] = 6
                elif event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    if condition:
                        gboard.sketch[row][col] = 7
                elif event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    if condition:
                        gboard.sketch[row][col] = 8
                elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    if condition:
                        gboard.sketch[row][col] = 9

                # checks for either delete or backspace button
                # checks to make sure the cell is editable (not in ogBoard (sketch value equals ten)), then sets both the board and sketch value back to 0
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    if gboard.sketch[row][col] != 10:
                        #this is the clear
                        gboard.sketch[row][col] = 0
                        gboard.board[row][col] = 0

                # checks for arrow input and changes which cell is highlighted
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if row > 0:
                        row -= 1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if row < 8:
                        row += 1
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if col < 8:
                        col += 1
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if col > 0:
                        col -= 1

                # checks to see if the board is completed and prints the end screen (dependent on all answers being correct or at least one incorrect answer)
                # AND ensures the board has all the numbers filled up are the same size with their respective color! :D
                if gboard.is_full():
                    gboard.loadGameBoard()
                    gboard.printEnteredNums()
                    gboard.printOgNums()
                    gboard.highLightBox(col, row)
                    pygame.display.update()
                    pygame.time.wait(500)
                    gboard.count += 1
                    gboard.checkWin()

                # if not completed, the cell remains highlighted
                else:
                    gboard.highLightBox(col, row)
                    gboard.selectedCell = (row, col)

            # once the game is over, it checks to see if user clicked the button
            if gboard.count == 2 and event.type == pygame.MOUSEBUTTONUP:
                # gets mouse position and whether the player won or lost (buttons differ on each end screen)
                x, y = event.pos[0], event.pos[1]
                win = gboard.checkWin()

                if (WIDTH // 2 - recWidth // 2) <= x <= (WIDTH // 2 + recWidth // 2) and (
                        HEIGHT // 2 - recHeight // 2 <= y <= HEIGHT // 2 + recHeight // 2):
                    # quits if the button on the winner screen is pressed
                    if win:
                        gboard.done()

                    # takes the player back to the starting screen if the button on the loser screen is pressed
                    else:
                        gboard.start_screen()
                        gboard.count = 0

        pygame.display.update()

if __name__ == "__main__":
    main()
