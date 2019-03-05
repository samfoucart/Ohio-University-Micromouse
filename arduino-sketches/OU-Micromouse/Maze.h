/*********************************************
 * @file    Maze.h
 * @date    February 2019
 * @author  Ohio University IEEE
 * 
 * 
**********************************************/

#ifndef MAZE_H
#define MAZE_H

#include "Cell.h"

class Maze
{
public:
    Maze();
    ~Maze();

    Cell * getCell(int x, int y){return data[y][x];}
    Cell * getCell(int unParsedCoordinate);

    /*
    int getUnparsedCoordinate(int x, int y);
    int parseX(int unParsedCoordinate);
    int parseY(int unParsedCoordinate);
    */

    void initializePerimiter();
    void initializeCenter();
    void initializeStart();

    void mouseMoveForward(){return;}
    void mouseScanWalls(){return;}
    void mouseTurnLeft(){return;}
    void mouseTurnRight(){return;}

    void floodFill(int x, int y);
    void floodFillCenter();
    void floodFillStart(){return;}

    void printFlood();


private:
    Cell * data[16][16];
    int mousePosition;
    int mouseDirection;
};

#endif
