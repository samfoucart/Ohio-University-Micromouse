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
        
    def getCell(self, x, y):
        return self.data[(x*16)+y]
        
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