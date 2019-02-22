#############################################################
# @file     mouse.py
# @date     February 2019
# @author   Ohio University IEEE
#
# This class holds information about the mouse itself,
# This includes:    Position
#                   Methods for Moving
#                   Direction
#                   
#
#############################################################

import sys
import API

class Mouse:

    def __init__(self):
        self.xPosition = 0
        self.yPosition = 0
        self.mouseDirection = "north"

    def getXPosition(self):
        return self.xPosition

    def getYPosition(self):
        return self.yPosition

    def getDirection(self):
        return self.mouseDirection

    def setXPosition(self, x):
        self.xPosition = x

    def setYPosition(self, y):
        self.yPosition = y

    def setDirection(self, entry):
        self.mouseDirection = entry

    def moveForward(self, maze):
        if (maze.getCell(self.xPosition, self.yPosition)).getWallDirection(self.mouseDirection) == True:
            return
        elif self.mouseDirection == "north":
            self.yPosition += 1
            API.moveForward()
        elif self.mouseDirection == "east":
            self.xPosition += 1
            API.moveForward()
        elif self.mouseDirection == "south":
            self.yPosition -= 1
            API.moveForward()
        elif self.mouseDirection == "west":
            self.xPosition -= 1
            API.moveForward()
        else:
            return

    def senseWalls(self, maze):
        return
            
        