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
import mouse

def log(string):
    sys.stderr.write("{}\n".format(string))

def main():
    log("hello")
    OUMaze = maze.Maze()
    OUMaze.loadPerimiter()
    OUMouse = mouse.Mouse()
    while(True):
        OUMouse.moveForward(OUMaze)


if __name__ == "__main__":
    main()