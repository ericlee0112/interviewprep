

class Rectangle:
    def __init__(self, color, topLeftCol, topLeftRow, bottomRightCol, bottomRightRow):
        self.color = color
        self.topLeftCol = topLeftCol
        self.topLeftRow = topLeftRow
        self.bottomRightCol = bottomRightCol
        self.bottomRightRow = bottomRightRow



class ASCIISolver:
    def __init__(self):
        self.canvas = [["" for _ in range(10)] for _ in range(6)]
    
    def drawRectangle(self, color, topLeftCol, topLeftRow, bottomRightCol, bottomRightRow):
        isValidCoordinates = self.validateInput(topLeftCol, topLeftRow, bottomRightCol, bottomRightRow)
        if isValidCoordinates == False:
            print("invalid coordinates")
            return

        for i in range(topLeftRow, bottomRightRow + 1):
            for j in range(topLeftCol, bottomRightCol + 1):
                self.canvas[i][j] = color

    
    def eraseArea(self, topLeftCol, topLeftRow, bottomRightCol, bottomRightRow):
        isValidCoordinates = self.validateInput(topLeftCol, topLeftRow, bottomRightCol, bottomRightRow)
        if isValidCoordinates == False:
            print("invalid coordinates")
            return

        for i in range(topLeftRow, bottomRightRow + 1):
            for j in range(topLeftCol, bottomRightCol + 1):
                self.canvas[i][j] = ""

    
    def dragAndDrop(self, selectCol, selectRow, releaseCol, releaseRow):
        isValidCoordinates = self.validateInput(selectCol, selectRow, releaseCol, releaseRow)
        if isValidCoordinates == False:
            print("invalid coordinates")
            return
        
        # check if self.canvas[selectRow][selectCol] is on a color, if true, move on with drag and drop
        if self.canvas[selectRow][selectCol] == "":
            return 
        
        colorOfChosenRectangle = self.canvas[selectRow][selectCol]

        # get topleft and bottomright coordinates of this rectangle
        topLeftRowOfRectangle, topLeftColOfRectangle, bottomRightRowOfRectangle, bottomRightColOfRectangle = self.findRectangleCoordinates(colorOfChosenRectangle, selectRow, selectCol)

        # determine the delta from [selectRow][selectCol] to [releaseRow][releaseCol]
        rowDelta = releaseRow - selectRow
        colDelta = releaseCol - selectCol

        # with the delta, determine what the new topLeftCol, topLeftRow, bottomRightCol, bottomRightRow will be for this new rectangle
        newTopLeftRowOfRectangle = topLeftRowOfRectangle + rowDelta
        newTopLeftColOfRectangle = topLeftColOfRectangle + colDelta
        newBottomRightRowOfRectangle = bottomRightRowOfRectangle + rowDelta
        newBottomRightColOfRectangle = bottomRightColOfRectangle + rowDelta

        # eraseArea
        self.eraseArea(topLeftColOfRectangle,topLeftRowOfRectangle, bottomRightColOfRectangle, bottomRightRowOfRectangle)

        # drawRectangle
        self.drawRectangle(colorOfChosenRectangle, newTopLeftColOfRectangle, newTopLeftRowOfRectangle, newBottomRightColOfRectangle, newBottomRightRowOfRectangle)
    
    
    def bringToFront(self, selectCol, selectRow):
        # input validation

        if self.canvas[selectRow][selectCol] == "":
            return 
        
        colorOfChosenRectangle = self.canvas[selectRow][selectCol]

        # get topleft and bottomright coordinates of this rectangle
        topLeftRowOfRectangle, topLeftColOfRectangle, bottomRightRowOfRectangle, bottomRightColOfRectangle = self.findRectangleCoordinates(colorOfChosenRectangle, selectRow, selectCol)

        # draw rectangle again
        self.drawRectangle(colorOfChosenRectangle, topLeftColOfRectangle, topLeftRowOfRectangle, bottomRightColOfRectangle, bottomRightRowOfRectangle)

    def printCanvas(self):
        print(self.canvas)

    # gets the top left and bottom right coordinates of rectangle chosen 
    def findRectangleCoordinates(self, color, row, col):
        topLeftRow = row
        topLeftCol = col

        while topLeftRow > 0 and self.canvas[topLeftRow][topLeftCol] == color:
            topLeftRow -= 1
        while topLeftCol > 0 and self.canvas[topLeftRow][topLeftCol] == color:
            topLeftCol -= 1

        bottomRightRow = row
        bottomRightCol = col

        while bottomRightRow < 5 and self.canvas[bottomRightRow][bottomRightCol] == color:
            bottomRightRow += 1
        
        while bottomRightCol < 9 and self.canvas[bottomRightRow][bottomRightCol] == color:
            bottomRightRow += 1
        
        return [topLeftRow, topLeftCol, bottomRightRow, bottomRightCol]


    # input validation method
    def validateInput(self, topLeftCol, topLeftRow, bottomRightCol, bottomRightRow):
        if topLeftCol >= 0 and topLeftCol < 10 and topLeftRow >= 0 and topLeftRow < 6 and bottomRightCol >= 0 and bottomRightCol < 10 and bottomRightRow >= 0 and bottomRightRow < 6:
            return True
        else:
            return False


    # point of entry   
    def parseCommand(self, commandString):
        tokens = commandString.split(" ")
        operation = tokens[0]
        # determine which operation to go with 
        if operation == "DRAW_RECTANGLE":
            # get parameters
            color = tokens[1]
            topLeftCol = tokens[2]
            topLeftRow = tokens[3]
            bottomRightCol = tokens[4]
            bottomRightRow = tokens[5]

            self.drawRectangle(color, topLeftCol, topLeftRow, bottomRightCol, bottomRightRow)
        
        elif operation == "DRAG_AND_DROP":
            # get parameters
            selectCol = tokens[1]
            selectRow = tokens[2]
            releaseCol = tokens[3]
            releaseRow = tokens[4]
            self.dragAndDrop(selectCol, selectRow, releaseCol, releaseRow)

        elif operation == "PRINT_CANVAS":
            self.printCanvas()
        
        elif operation == "ERASE_AREA":
            topLeftCol = tokens[1]
            topLeftRow = tokens[2]
            bottomRightCol = tokens[3]
            bottomRightRow = tokens[4]
            self.eraseArea(topLeftCol, topLeftRow, bottomRightCol, bottomRightRow)
        
        elif operation == "BRING_TO_FRONT":
            col = tokens[1]
            row = tokens[2]
            self.bringToFront(col, row)
    
        else:
            print("invalid command")


