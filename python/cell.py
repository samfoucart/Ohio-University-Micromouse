#############################################################
# @file     cell.py
# @date     February 2019
# @author   Ohio University IEEE
#
# This class contains the the wall and flood fill
# information. It is meant to be put into a maze class
# that holds an array of cell items so that the wall
# and flood fill information can be accessed for each
# individual cell.
#
#############################################################
import sys
import API

""" @brief  This class contains the the wall and flood fill
    information. It is meant to be put into a maze class
    that holds an array of cell items so that the wall
    and flood fill information can be accessed for each
    individual cell.
"""

class Cell:
    """ @class Cell
        Contains information on whether the mouse has visited
        each cell, where the walls are, and the flood fill values
    """

    def __init__(self):
        self.hasWallNorth = False
        self.hasWallEast = False 
        self.hasWallSouth = False
        self.hasWallWest = False
        self.hasBeenVisited = False
        self.hasBeenFilled = False
        self.floodFillValue = -1

    """Getters"""
    def getWallNorth(self): 
        return self.hasWallNorth

    def getWallEast(self): 
        return self.hasWallEast

    def getWallSouth(self):
        return self.hasWallSouth

    def getWallWest(self):
        return self.hasWallWest

    def getWallDirection(self, direction):
        if direction == "north":
            return self.hasWallNorth
        elif direction == "east":
            return self.hasWallEast
        elif direction == "south":
            return self.hasWallSouth
        elif direction == "west":
            return self.hasWallWest
        else:
            return

    def getBeenVisited(self):
        return self.hasBeenVisited

    def getFloodFillValue(self):
        return self.floodFillValue

    """Setters"""
    """ These set the value of the corresponding variable
        to be equal to entry
        @param  entry (Input) The value you want the corresponding
        variable to be set to.
    """ 
    def setWallNorth(self, entry):
        self.hasWallNorth = entry

    def setWallEast(self, entry):
        self.hasWallEast = entry

    def setWallSouth(self, entry):
        self.hasWallSouth = entry

    def setWallWest(self, entry):
        self.hasWallWest = entry

    def setFloodFillValue(self, entry):
        self.floodFillValue = entry

    def setHasBeenVisited(self, entry):
        self.hasBeenVisited = entry

    

        



