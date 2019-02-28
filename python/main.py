#############################################################
# @file     main.py
# @date     February 2019
# @author   Ohio University IEEE
#
# This is the main function of the mouse.
#
#############################################################
import API
import sys
import maze

def log(string):
    sys.stderr.write("{}\n".format(string))

def main():
    #log("hello")
    OUMaze = maze.Maze()
    
    OUMaze.loadPerimiter()
    #for value in range(0, 256):
    #    API.setText(OUMaze.parseX(value),OUMaze.parseY(value),str(OUMaze.getCell(OUMaze.parseX(value),OUMaze.parseY(value)).getWallSouth()))
    
    OUMaze.colorCenter()
    OUMaze.floodFill(0,0)
    #OUMaze.floodFillCenter()
    
    while(True):
        OUMaze.mouseScanWalls()
        if API.wallLeft() == False:
            OUMaze.mouseTurnLeft()
        if API.wallFront() == True:
            OUMaze.mouseTurnRight()
        OUMaze.mouseMoveForward()
    




if __name__ == "__main__":
    main()