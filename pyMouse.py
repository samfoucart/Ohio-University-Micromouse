#############################################################
# @file     maze.py
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
    mainMaze = maze.Maze
    mainMaze.loadPerimiter

if __name__ == "__main__":
    main()