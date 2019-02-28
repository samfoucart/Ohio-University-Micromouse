#include "Maze.h"
#include "Cell.h"
#include <iostream>

int main()
{
    Maze OUMaze;
    OUMaze.initializePerimiter();
    OUMaze.initializeCenter();
    for (int j = 4; j < 10; ++j)
    {
        //OUMaze.getCell(j, 11)->setWallSouth(true);
        OUMaze.getCell(j, 10)->setWallNorth(true);
    }

    OUMaze.floodFillCenter();
    OUMaze.printFlood();
}