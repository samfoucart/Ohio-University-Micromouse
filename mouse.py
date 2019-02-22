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
        xPosition = 0
        yPosition = 0
        direction = "north"

    def getXPosition(self):
        return self.xPosition

    def getYPosition(self):
        return self.yPosition

    def getDirection(self):
        return self.direction

    def setXPosition(self, x):
        self.xPosition = x

    def setYPosition(self, y):
        self.yPosition = y

    def setDirection(self, entry):
        self.direction = entry

    def moveForward(self):
        print("xxx")