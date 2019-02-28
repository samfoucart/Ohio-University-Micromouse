#############################################################
# @file     maze.py
# @date     February 2019
# @author   Ohio University IEEE
#
# This class is a container class for the maze. It holds
# cell objects which are imported from cell.py
#
#############################################################

import sys
import API
import cell
import floodFillStack

""" @brief  This class is a container class for the maze. It holds
    cell objects which are imported from cell.py
"""

""" @class Maze
        This class is a container of Cells
"""
class Maze:

    """ Constructor
        @see loadPerimeter
    """
    def __init__(self):
        self.data = []
        for i in range(0,256):
            self.data.append(cell.Cell())
            
        self.floodFillStack = floodFillStack.floodFillStack()


        self.mousePosition = 0
        self.mouseDirection = "north"


    """ getUnparsedCoordinate This method returns a integer that can be parsed to 
        determine the x and y coordinates of a cell
        @param x this is the x coordinate of a cell
        @param y this is the y coordinate of a cell
        @return this is an the major row index of the 
        array
    """
    def getUnparsedCoordinate(self, x, y):
        return (x*16)+y

    """ parseX This method converts the major row index of the 
        array into a X coordinate
        @param unParsedCoordinate This is the row major index
        of the one dimensional data array
        @return an integer value of the X coordinate
    """
    def parseX(self, unParsedCoordinate):
        return unParsedCoordinate % 16

    """ parseY This method converts the major row index of the 
        array into a Y coordinate
        @param unParsedCoordinate This is the row major index
        of the one dimensional data array
        @return an integer value of the Y coordinate
    """
    def parseY(self, unParsedCoordinate):
        return int((unParsedCoordinate - (unParsedCoordinate % 16)) / 16)

    """ getCell This method returns a cell given
        the (x,y) coordinates
        @param x the X coordinate of the cell
        @param y the y coordinate of the cell
    """
    def getCell(self, x, y):
        return self.data[self.getUnparsedCoordinate(x, y)]

    
    """ This function sets the outer walls of a 16x16 maze
        It should be called before anything else, but is not included in the
        constructor for added freedom.
    """
    def loadPerimiter(self):
        for i in range(0,16):
            for j in range(0,16):
                if i == 0:
                    self.data[self.getUnparsedCoordinate(j,i)].setWallSouth(True)
                    API.setWall(j, i, "s")
                
                if i == 15:
                    self.data[self.getUnparsedCoordinate(j, i)].setWallNorth(True)
                    API.setWall(j, i, "n")

                if j == 0:
                    self.data[self.getUnparsedCoordinate(j, i)].setWallWest(True)
                    API.setWall(j, i, "w")

                if j == 15:
                    self.data[self.getUnparsedCoordinate(j, i)].setWallEast(True)
                    API.setWall(j, i, "e")

    """ This function moves the mouse forward and assumes
        that the mouse has already scanned for walls.
    """
    def mouseMoveForward(self):
        if API.wallFront() == True:
            """ If the cell where the mouse is"""
            return
        elif self.mouseDirection == "north":
            self.mousePosition += 16
            API.moveForward()
        elif self.mouseDirection == "east":
            self.mousePosition += 1
            API.moveForward()
        elif self.mouseDirection == "south":
            self.mousePosition -= 16
            API.moveForward()
        elif self.mouseDirection == "west":
            self.mousePosition -= 1
            API.moveForward()
        else:
            return

    """ This function senses the walls adjacent to the mouse.
        It also adds the wall data to the neighboring cells
    """
    def mouseScanWalls(self):
        if self.mouseDirection == "north":
            self.data[self.mousePosition].setWallWest(API.wallLeft())
            self.data[self.mousePosition].setWallNorth(API.wallFront())
            self.data[self.mousePosition].setWallEast(API.wallRight())

            if API.wallLeft() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "w")
                if self.parseX(self.mousePosition) != 0:
                    self.data[self.mousePosition - 1].setWallEast(True)
                    API.setText(self.parseX(self.mousePosition - 1), self.parseY(self.mousePosition), "->")

            if API.wallFront() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "n")
                if self.parseY(self.mousePosition) != 15:
                    self.data[self.mousePosition + 16].setWallSouth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition + 16), "v")

            if API.wallRight() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "e")
                if self.parseX(self.mousePosition) != 15:
                    self.data[self.mousePosition + 1].setWallWest(True)
                    API.setText(self.parseX(self.mousePosition + 1), self.parseY(self.mousePosition), "<-")

        if self.mouseDirection == "east":
            self.data[self.mousePosition].setWallNorth(API.wallLeft())
            self.data[self.mousePosition].setWallEast(API.wallFront())
            self.data[self.mousePosition].setWallSouth(API.wallRight())


            if API.wallLeft() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "n")
                if self.parseY(self.mousePosition) != 15:
                    self.data[self.mousePosition + 16].setWallSouth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition + 16), "v")

            if API.wallFront() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "e")
                if self.parseX(self.mousePosition) != 15:
                    self.data[self.mousePosition + 1].setWallWest(True)
                    API.setText(self.parseX(self.mousePosition + 1), self.parseY(self.mousePosition), "<-")

            if API.wallRight() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "s")
                if self.parseY(self.mousePosition) != 0:
                    self.data[self.mousePosition - 16].setWallNorth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition - 16), "^")

        if self.mouseDirection == "south":
            self.data[self.mousePosition].setWallEast(API.wallLeft())
            self.data[self.mousePosition].setWallSouth(API.wallFront())
            self.data[self.mousePosition].setWallWest(API.wallRight())


            if API.wallLeft() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "e")
                if self.parseX(self.mousePosition) != 15:
                    self.data[self.mousePosition + 1].setWallWest(True)
                    API.setText(self.parseX(self.mousePosition + 1), self.parseY(self.mousePosition), "<-")

            if API.wallFront() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "s")
                if self.parseY(self.mousePosition) != 0:
                    self.data[self.mousePosition - 16].setWallNorth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition - 16), "^")

            if API.wallRight() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "w")
                if self.parseX(self.mousePosition) != 0:
                    self.data[self.mousePosition - 1].setWallEast(True)
                    API.setText(self.parseX(self.mousePosition - 1), self.parseY(self.mousePosition), "->")

        if self.mouseDirection == "west":
            self.data[self.mousePosition].setWallSouth(API.wallLeft())
            self.data[self.mousePosition].setWallWest(API.wallFront())
            self.data[self.mousePosition].setWallNorth(API.wallRight())


            if API.wallLeft() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "s")
                if self.parseY(self.mousePosition) != 0:
                    self.data[self.mousePosition - 16].setWallNorth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition - 16), "^")

            if API.wallFront() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "w")
                if self.parseX(self.mousePosition) != 0:
                    self.data[self.mousePosition - 1].setWallEast(True)
                    API.setText(self.parseX(self.mousePosition - 1), self.parseY(self.mousePosition), "->")

            if API.wallRight() == True:
                API.setWall((self.parseX(self.mousePosition)), (self.parseY(self.mousePosition)), "n")
                if self.parseY(self.mousePosition) != 15:
                    self.data[self.mousePosition + 16].setWallSouth(True)
                    API.setText(self.parseX(self.mousePosition), self.parseY(self.mousePosition + 16), "v")

            

    def mouseTurnLeft(self):
        if self.mouseDirection == "north":
            self.mouseDirection = "west"
        elif self.mouseDirection == "east":
            self.mouseDirection = "north"
        elif self.mouseDirection == "south":
            self.mouseDirection = "east"
        elif self.mouseDirection == "west":
            self.mouseDirection = "south"
        else:
            return

        API.turnLeft()

    def mouseTurnRight(self):
        if self.mouseDirection == "north":
            self.mouseDirection = "east"
        elif self.mouseDirection == "east":
            self.mouseDirection = "south"
        elif self.mouseDirection == "south":
            self.mouseDirection = "west"
        elif self.mouseDirection == "west":
            self.mouseDirection = "north"
        else:
            return
        
        API.turnRight()

    def mouseTurnAround(self):
        self.mouseTurnRight()
        self.mouseTurnRight()

        API.turnRight()
        API.turnRight()

    def colorCenter(self):
        for i in range(7,9):
            for j in range(7,9):
                API.setColor(i, j, 'G')
                self.getCell(i,j).setFloodFillValue(0)
                API.setText(i, j, "0")

    def floodFill(self, x, y):
        """ As of writing this, I don't think we should do this
            recursively. The wikipedia page only gives recursive 
            examples, but their examples are different than what
            we're doing anyway.
            From https://www.youtube.com/watch?v=he3y_U7M8ng :
            *   We need an empty stack to store cells
            *   Whenever we discover a new wall, we push the current
                cell into the stack and the adjacent cells to the 
                new wall that we discovered
                *   currCell <- pop the top of the stack
                *   The distance of currCell should be the minimum 
                    open neighbor distance + 1
                *   If it is not, then set it to that value and push
                    all open neighbors to the stack
            *   This probably doesn't apply to a teensy specifically
                but this is good information to know. When working on
                embedded systems, recursion is bad because it wastes
                memory. It is much more memory efficient to store 
                recursive information on your own stack. It is also
                bad to create this stack within the function. In memory,
                all function data structures are put onto the "system
                stack." On an embedded system, this stack is very memory
                constrained, so it is better practice to make a global
                variable to hold this stack, so that the rest of your
                functions have enough memory on the system stack.
        """
        #if self.floodFillStack.isEmpty() == False:
        #    return
        # if no wall in a certain direction, look at adjacent cell in that direction
        # if adjacent cell flood fill value is <= current cell and not -1, do nothing
        # if adjacent cell flood fill value is > current cell or is -1, 
        #   make adjacent cell value currentcellvalue + 1
        #   floodFill(adjacentCell);
        # return

        
        # Look Up
        #API.setText(x,y+1, "hello")
        if self.getCell(x,y).getWallNorth() == False:
            #API.setText(x,y, str((y*16)+x))
            if (self.getCell(x,y+1).getFloodFillValue() > self.getCell(x,y).getFloodFillValue()) or (self.getCell(x,y+1).getFloodFillValue() == -1):
                self.getCell(x,y+1).setFloodFillValue(self.getCell(x,y).getFloodFillValue() + 1)
                API.setText(x,y + 1,str(self.getCell(x,y + 1).getFloodFillValue()))
                self.floodFill(x, y + 1)
        
        # Look Right
        if self.getCell(x,y).getWallEast() == False:
            if self.getCell(x+1,y).getFloodFillValue() > self.getCell(x,y).getFloodFillValue() or self.getCell(x+1,y).getFloodFillValue() == -1:
                self.getCell(x+1, y).setFloodFillValue(self.getCell(x,y).getFloodFillValue() + 1)
                API.setText(x+1, y, str(self.getCell(x + 1, y).getFloodFillValue()))
                self.floodFill(x + 1, y)
        
        
        # Look Left
        if self.getCell(x,y).getWallWest() == False:
            if self.getCell(x - 1, y).getFloodFillValue() > self.getCell(x,y).getFloodFillValue() or self.getCell(x - 1,y).getFloodFillValue() == -1:
                self.getCell(x - 1, y).setFloodFillValue(self.getCell(x,y).getFloodFillValue() + 1)
                API.setText(x - 1, y, str(self.getCell(x - 1, y).getFloodFillValue()))
                self.floodFill(x - 1, y)
        
        # Look Down
        if self.getCell(x,y).getWallSouth() == False:
            if self.getCell(x, y - 1).getFloodFillValue() > self.getCell(x,y).getFloodFillValue() or self.getCell(x, y - 1).getFloodFillValue() == -1:
                self.getCell(x, y - 1).setFloodFillValue(self.getCell(x,y).getFloodFillValue() + 1)
                API.setText(x, y - 1, str(self.getCell(x, y - 1).getFloodFillValue()))
                self.floodFill(x, y - 1)
        
        
        

        return

    def floodFillCenter(self):
        for i in range(7, 9):
            for j in range(7, 9):
                self.floodFill(j,i)
                    