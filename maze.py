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

""" @brief  This class is a container class for the maze. It holds
    cell objects which are imported from cell.py
"""

class Maze:
    """ @class Maze
        This class is a container of Cells
    """

    def __init__(self):
        self.data = []
        for i in range(0,256):
            self.data.append(cell.Cell())

    

    
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
        return (unParsedCoordinate - (unParsedCoordinate % 16)) / 16

    """ parseY This method converts the major row index of the 
        array into a Y coordinate

        @param unParsedCoordinate This is the row major index
        of the one dimensional data array
        @return an integer value of the Y coordinate
    """
    def parseY(self, unParsedCoordinate):
        return unParsedCoordinate % 16

    """ getCell This method returns a cell given
        the (x,y) coordinates

        @param x the X coordinate of the cell
        @param y the y coordinate of the cell
    """
    def getCell(self, x, y):
        return self.data[self.getUnparsedCoordinate(x,y)]
    
    def getCell(self, unParsedCoordinate):
        return self.data[unParsedCoordinate]

        
    def loadPerimiter(self):
        for i in range(0,16):
            for j in range(0,16):
                if i == 0:
                    if j == 0:
                        self.data[(i*16)+j].setWallSouth(True)
                        self.data[(i*16)+j].setWallWest(True)
                        API.setWall(i, j, "s")
                        API.setWall(i, j, "w")
                    elif j == 15:
                        self.data[(i*16)+j].setWallNorth(True)
                        self.data[(i*16)+j].setWallWest(True)
                        API.setWall(i, j, "n")
                        API.setWall(i, j, "w")
                    else:
                        self.data[(i*16)+j].setWallWest(True)
                        API.setWall(i, j, "w")
                
                if i == 15:
                    if j == 0:
                        self.data[(i*16)+j].setWallSouth(True)
                        self.data[(i*16)+j].setWallEast(True)
                        API.setWall(i, j, "s")
                        API.setWall(i, j, "e")
                    elif j == 15:
                        self.data[(i*16)+j].setWallNorth(True)
                        self.data[(i*16)+j].setWallEast(True)
                        API.setWall(i, j, "n")
                        API.setWall(i, j, "e")
                    else:
                        self.data[(i*16)+j].setWallEast(True)
                        API.setWall(i, j, "e")

                if j == 0 and (i != 0 or i != 15):
                    self.data[(i*16)+j].setWallSouth(True)
                    API.setWall(i, j, "s")

                if j == 15 and (i != 0 or i != 15):
                    self.data[(i*16)+j].setWallNorth(True)
                    API.setWall(i, j, "n")
  