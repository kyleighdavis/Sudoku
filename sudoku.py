import pygame, sys
from constants import *
from sudoku_generator import *

class Sudoku:
    def __init__(self):
        #initializes screen
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Group 20 Sudoku")

        #count will increase to 1 after start screen and after the board is complete it will increase to 2
        #it tells the computer when to change screens
        self.count = 0
        #other constants:
        #gameMode will hold how many numbers are hidden
        #selectedCell starts the cell not on the board
        self.gameMode = 0
        self.selectedCell = (-1, -1)

        #3 boards of numbers:
        #board contains all numbers on the board that are displayed (given and inputted)
        #ogBoard contains all the numbers visible to the player upon the game starting
        #sketch contains all the user's sketch values and prevents the user from changing a visible number (ogBoard)
        self.board = []
        self.ogBoard = []
        self.sketch = []

    #makes a new sketch pad list
    #comparing to the ogBoard, every box that has it's value hidden gets assigned a 0 and any visible value is assigned 10 to prevent changes from the user
    #returns sketch list
    def makeEmptySketch(self,board):
        self.sketch = []
        for i in board:
            row = []
            for j in i:
                if j != 0:
                    row.append(10)
                else:
                    row.append(0)
            self.sketch.append(row)

    #makes the sudoku board and, based on difficulty, hides the appropriate number of values
    #returns four lists: board with hidden values, copy of that board, answer key, and editable board
    #returns board list, sketch list, ogBoard list
    def makeSudoku(self,gameMode):
        game = generate_sudoku(9, gameMode)
        self.board = game
        #makes copy of original board
        self.ogBoard = []
        for i in self.board:
            self.ogBoard.append(i[:])
        #makes the sketch list with previously described conditions
        self.makeEmptySketch(self.board)

    #sets the board to the ogBoard and creates a new sketch list with 0s in place of hidden values and 10s in place of visible values
    #returns board list and sketch list
    def reset(self,ogBoard):
        self.makeEmptySketch(self.ogBoard)
        self.board = []
        for i in self.ogBoard:
            self.board.append(i[:])

    #quits game
    def done(self):
        pygame.quit()
        sys.exit()

    #prints the starting screen
    #returns None
    def start_screen(self):
        #fills background
        self.screen.fill(fsBackColor)

        #prints welcome text
        welcome = pygame.font.Font(None, WIDTH//8).render("Welcome To Sudoku!", 0, startTitleText)
        wLoc = welcome.get_rect(center=(WIDTH / 2, HEIGHT / 4))
        self.screen.blit(welcome, wLoc)

        #prints good luck message
        hTxt = pygame.font.Font(None, WIDTH // 10).render("Good Luck :)", 0, startTitleText)
        hLoc = hTxt.get_rect(center = (WIDTH / 2, HEIGHT / 3))
        self.screen.blit(hTxt, hLoc)

        #prints instruction
        gameModeTxt = pygame.font.Font(None, WIDTH // 10).render("Select game mode: ", 0, startTitleText)
        gLoc = gameModeTxt.get_rect(center = (WIDTH / 2, HEIGHT / 2))
        self.screen.blit(gameModeTxt, gLoc)

        #prints three buttons
        pygame.draw.rect(self.screen, startButtonColors, pygame.Rect(WIDTH // 22, HEIGHT * 5 // 8, recWidth, recHeight))
        pygame.draw.rect(self.screen, startButtonColors, pygame.Rect(WIDTH * 8 // 22, HEIGHT * 5 // 8, recWidth, recHeight))
        pygame.draw.rect(self.screen, startButtonColors, pygame.Rect(WIDTH * 15 // 22, HEIGHT * 5 // 8, recWidth, recHeight))

        #prints lines around buttons
        lineWidth = 7
        #button 1
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH // 22, HEIGHT *5 // 8), (WIDTH // 22 + recWidth, HEIGHT * 5 // 8), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH // 22, HEIGHT * 5 // 8 + recHeight), (WIDTH // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH // 22, HEIGHT * 5 // 8), (WIDTH // 22, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH // 22 + recWidth, HEIGHT * 5 // 8), (WIDTH // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)
        #button 2
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 8 // 22, HEIGHT * 5 // 8), (WIDTH * 8 // 22 + recWidth, HEIGHT * 5 // 8), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 8 // 22, HEIGHT * 5 // 8 + recHeight), (WIDTH * 8 // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 8 // 22, HEIGHT * 5 // 8), (WIDTH * 8 // 22, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 8 // 22 + recWidth, HEIGHT * 5 // 8), (WIDTH * 8 // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)
        #button 3
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 15 // 22, HEIGHT * 5 // 8), (WIDTH * 15 // 22 + recWidth, HEIGHT * 5 // 8), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 15 // 22, HEIGHT * 5 // 8 + recHeight),(WIDTH * 15 // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 15 // 22, HEIGHT * 5 // 8), (WIDTH * 15 // 22, HEIGHT * 5 // 8 + recHeight), lineWidth)
        pygame.draw.line(self.screen, darkButtonCol, (WIDTH * 15 // 22 + recWidth, HEIGHT * 5 // 8), (WIDTH * 15 // 22 + recWidth, HEIGHT * 5 // 8 + recHeight), lineWidth)

        #prints text of difficulty on each button
        #easy
        button1Txt = pygame.font.Font(None, WIDTH // 15).render("easy", 0, buttonTextCol)
        b1Loc = button1Txt.get_rect(center = (WIDTH // 22 + (recWidth // 2), HEIGHT * 5 // 8 + (recHeight // 2)))
        self.screen.blit(button1Txt, b1Loc)
        #medium
        button2Txt = pygame.font.Font(None, WIDTH // 15).render("medium", 0, buttonTextCol)
        b2Loc = button2Txt.get_rect(center = (WIDTH * 8 // 22 + (recWidth // 2), HEIGHT * 5 // 8 + (recHeight // 2)))
        self.screen.blit(button2Txt, b2Loc)
        #hard
        button3Txt = pygame.font.Font(None, WIDTH // 15).render("hard", 0, buttonTextCol)
        b3Loc = button3Txt.get_rect(center = (WIDTH * 15 // 22 + (recWidth // 2), HEIGHT * 5 // 8 + (recHeight // 2)))
        self.screen.blit(button3Txt, b3Loc)

    #with the x and y coordinate of the mouse upon clicking a box, this finds out which difficulty was chosen
    #returns the number of cells that should be empty
    #returns zero if no button is hit
    def setGameMode(self,x, y):
        #checks for easy button
        if (WIDTH // 22 <= x <= (WIDTH // 22 + recWidth)) and ((HEIGHT * 5 // 8) <= y <= HEIGHT * 5 // 8 + recHeight):
            return 30
        #checks for medium
        elif (WIDTH * 8 // 22 <= x <= (WIDTH * 8 // 22 + recWidth)) and ((HEIGHT * 5 // 8) <= y <= HEIGHT * 5 // 8 + recHeight):
            return 40
        #checks for hard
        elif (WIDTH * 15 // 22 <= x <= (WIDTH * 15 // 22 + recWidth)) and ((HEIGHT * 5 // 8) <= y <= HEIGHT * 5 // 8 + recHeight):
            return 50
        return 0

    #checks to see if user hits one of the bottom buttons during a sudoku game and updates the screen accordingly
    #returns the value of count and whether the program is done or not
    def checkBottomButtons(self,x, y):
        #checks to see if reset button was clicked, then resets the board to original set up
        if WIDTH // 22 <= x <= (WIDTH // 22 + recWidth) and HEIGHT * 53 // 64 <= y <= (HEIGHT * 53 // 64 + recHeight):
            self.count=1
            return True
        #checks to see if restart button was clicked, then brings user back to start screen
        elif WIDTH * 8 // 22 <= x <= (WIDTH * 8 // 22 + recWidth) and HEIGHT * 53 // 64 <= y <= (HEIGHT * 53 // 64 + recHeight):
            self.start_screen()
            self.count = 0
            return False
        #check to see if quit button was clicked and ends the program
        elif WIDTH * 15 // 22 <= x <= (WIDTH * 15 // 22 + recWidth) and HEIGHT * 53 // 64 <= y <= (HEIGHT * 53 // 64 + recHeight):
            self.done()
            self.count=1
        return False

    #prints the game-over screen
    #returns None
    def gameOverScreen(self):
        #fills background
        self.screen.fill(fsBackColor)
        #prints game-over text
        over = pygame.font.Font(None, WIDTH // 6).render("Game Over :(", 0, startTitleText)
        oLoc = over.get_rect(center = (WIDTH / 2, HEIGHT / 3))
        self.screen.blit(over, oLoc)
        #prints button
        pygame.draw.rect(self.screen, startButtonColors, pygame.Rect(WIDTH // 2-recWidth//2, HEIGHT  // 2-recHeight//2, recWidth, recHeight))
        #prints restart text
        restartTxt = pygame.font.Font(None, WIDTH // 10).render("restart", 0, buttonTextCol)
        restartloc = restartTxt.get_rect(center = (WIDTH // 2 , HEIGHT // 2 ))
        self.screen.blit(restartTxt, restartloc)

    #prints the game-won screen
    #returns None
    def wonScreen(self):
        #fills background
        self.screen.fill(fsBackColor)
        #print game-won text
        won = pygame.font.Font(None, WIDTH // 6).render("Game Won!", 0, startTitleText)
        wLoc = won.get_rect(center = (WIDTH / 2, HEIGHT / 3))
        self.screen.blit(won, wLoc)
        # print button
        pygame.draw.rect(self.screen, startButtonColors,pygame.Rect(WIDTH // 2 - recWidth // 2, HEIGHT // 2 - recHeight // 2, recWidth, recHeight))
        # print exit text
        exitTxt = pygame.font.Font(None, WIDTH // 10).render("exit", 0, buttonTextCol)
        exitloc = exitTxt.get_rect(center = (WIDTH // 2, HEIGHT // 2))
        self.screen.blit(exitTxt, exitloc)

    #prints the sketch numbers in the top left corner in smaller purple font
    #goes through the sketch list
    #if the value is 0 or 10, then it will not print anything, but if the value is something else it will print inputted value
    #returns None
    def printSketchNums(self):
        for row in range(len(self.sketch)):
            for col in range(len(self.sketch[0])):
                value = self.sketch[row][col]
                if value != 0 and value != 10:
                    skTxt = pygame.font.Font(None, numSizeSmall).render(str(value), 0, sketchNumColor)
                    skLoc = skTxt.get_rect(center = (col * cellWidth + cellWidth // 4, row * cellHeight + cellHeight // 4))
                    self.screen.blit(skTxt, skLoc)

    #print the number on the board list in light pink, but if the number is 0 nothing is printed
    #returns None
    def printEnteredNums(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                value = self.board[row][col]
                if value != 0:
                    valTxt = pygame.font.Font(None, numSizeBig).render(str(value), 0, enterNumColor)
                    valLoc = valTxt.get_rect(center = (col*cellWidth+cellWidth // 2, row*cellHeight+cellHeight // 2))
                    self.screen.blit(valTxt, valLoc)

    #takes the values from ogBoard and prints them out in dark pink
    def printOgNums(self):
        for row in range(len(self.ogBoard)):
            for col in range(len(self.ogBoard[0])):
                value = self.ogBoard[row][col]
                if value != 0:
                    ogTxt = pygame.font.Font(None, numSizeBig).render(str(value), 0, ogNumColor)
                    ogLoc = ogTxt.get_rect(center = (col * cellWidth + cellWidth // 2, row * cellHeight + cellHeight // 2))
                    self.screen.blit(ogTxt, ogLoc)

    #prints all the numbers by calling all print numbers functions
    def printAllNums(self):
        self.printEnteredNums()
        self.printOgNums()
        self.printSketchNums()

    #prints the Sudoku board screen
    #returns None
    def loadGameBoard(self):
        #fills background
        self.screen.fill(gameBackColor)
        #prints the grid lines
        lineWidth=0
        for i in range(10):
            if i % 3 == 0:
                lineWidth = thickLine
            else:
                lineWidth = thinLine
            pygame.draw.line(self.screen, gridColor, (0, i * cellHeight), (WIDTH, i * cellHeight), lineWidth)
        for i in range(10):
            if i % 3 == 0:
                lineWidth = thickLine
            else:
                lineWidth = thinLine
            pygame.draw.line(self.screen, gridColor, (i * cellWidth,0), (i * cellWidth,(WIDTH - (WIDTH // 10))), lineWidth)

        #prints the buttons at the bottom of the screen
        bHeight = HEIGHT * 53 // 64
        pygame.draw.rect(self.screen, sudokuButtonColor, pygame.Rect(WIDTH // 22, bHeight, recWidth, recHeight))
        pygame.draw.rect(self.screen, sudokuButtonColor, pygame.Rect(WIDTH * 8 // 22,  bHeight, recWidth, recHeight))
        pygame.draw.rect(self.screen, sudokuButtonColor, pygame.Rect(WIDTH * 15 // 22,  bHeight, recWidth, recHeight))

        #prints lines around buttons
        lineWidth = 5
        #button 1
        bWidth1 = WIDTH // 22
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth1, bHeight), (bWidth1 + recWidth, bHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth1, bHeight + recHeight),(bWidth1 + recWidth, bHeight + recHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth1, bHeight), (bWidth1, bHeight + recHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth1 + recWidth, bHeight),(bWidth1 + recWidth, bHeight+ recHeight), lineWidth)
        #button 2
        bWidth2 = WIDTH // 22 * 8
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth2, bHeight), (bWidth2 + recWidth, bHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth2, bHeight + recHeight), (bWidth2 + recWidth, bHeight + recHeight),lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth2, bHeight), (bWidth2, bHeight + recHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth2 + recWidth, bHeight), (bWidth2 + recWidth, bHeight + recHeight), lineWidth)
        #button 3
        bWidth3 = WIDTH // 22 * 15
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth3, bHeight), (bWidth3 + recWidth, bHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth3, bHeight + recHeight), (bWidth3 + recWidth, bHeight + recHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth3, bHeight), (bWidth3, bHeight + recHeight), lineWidth)
        pygame.draw.line(self.screen, ButtonHighLight, (bWidth3 + recWidth, bHeight), (bWidth3 + recWidth, bHeight + recHeight), lineWidth)

        #button text
        #reset
        resetTxt = pygame.font.Font(None, WIDTH // 15).render("reset", 0, sButtonTxtColor)
        resetLoc = resetTxt.get_rect(center = (WIDTH // 22 + (recWidth // 2), bHeight + (recHeight // 2)))
        self.screen.blit(resetTxt, resetLoc)
        #restart
        restartTxt = pygame.font.Font(None, WIDTH // 15).render("restart", 0, sButtonTxtColor)
        restartLoc = restartTxt.get_rect(center = (WIDTH * 8 // 22 + (recWidth // 2), bHeight  + (recHeight // 2)))
        self.screen.blit(restartTxt, restartLoc)
        #exit
        exitTxt = pygame.font.Font(None, WIDTH // 15).render("exit", 0, sButtonTxtColor)
        exitLoc = exitTxt.get_rect(center = (WIDTH * 15 // 22 + (recWidth // 2), bHeight + (recHeight // 2)))
        self.screen.blit(exitTxt, exitLoc)

        self.printAllNums()

    #prints the board and then prints a red box around the selected bow in row y and col x
    #returns None
    def highLightBox(self,x, y):
        self.loadGameBoard()
        lineWidth = 4
        x1 = x * cellWidth
        x2 = x1 + cellWidth
        y1 = y * cellHeight
        y2 = y1 + cellHeight
        line1 = pygame.draw.line(self.screen, gridRed, (x1, y1), (x2, y1), lineWidth)
        line2 = pygame.draw.line(self.screen, gridRed, (x1, y1), (x1, y2), lineWidth)
        line3 = pygame.draw.line(self.screen, gridRed, (x1, y2), (x2, y2), lineWidth)
        line4 = pygame.draw.line(self.screen, gridRed, (x2, y1), (x2, y2), lineWidth)


    #checks to see if board is completed, meaning there are no 0s in the board list
    #if there are no 0 values, then it returns True otherwise it returns False
    #returns boolean
    def is_full(self):
        #checks to see if the list has any 0s
        for i in self.board:
            for j in i:
                if j==0:
                    return False
        return True

    #checks to see if the number at specified row and column is valid
    #returns True if so and returns False if not
    #returns boolean
    def checkValidAnswer(self,row, col, num):
        #checks to see if number is a duplicate within row
        for i in range(len(self.board[row])):
            if self.board[row][i] == num and i != col:
                return False
        #checks to see if number is a duplicate within column
        for j in range(len(self.board)):
            if self.board[j][col] == num and j != row:
                return False

        #checks to see if number is a duplicate within the 3x3 box
        for r in range((row // 3) * 3, (row // 3) * 3 + 3):
            for c in range((col // 3) * 3, (col // 3) * 3 + 3):
                if self.board[r][c] == num and (r != row or c != col):
                    return False
        return True

    #check to see if all the numbers in the board are valid
    #returns True if so and returns False if not
    #returns boolean
    def checkWin(self):
        for row in range (len(self.board)):
            for col in range (len(self.board[0])):
                if not(self.checkValidAnswer(row, col, self.board[row][col])):
                    self.gameOverScreen()
                    return False
        self.wonScreen()
        return True
