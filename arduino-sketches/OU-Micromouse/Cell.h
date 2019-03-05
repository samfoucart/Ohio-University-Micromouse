/*********************************************
 * @file    Cell.h
 * @date    February 2019
 * @author  Ohio University IEEE
 * 
 * 
**********************************************/

#ifndef CELL_H
#define CELL_H

class Cell
{
public:
    typedef unsigned char byte;
    
    Cell()
    {
        hasWallNorth = false;
        hasWallEast = false;
        hasWallSouth = false;
        hasWallWest = false;
        hasBeenVisited = false;
        hasBeenFilled = false;
        floodFillValue = -1;
    }
    
    bool getWallNorth(){return hasWallNorth;}
    bool getWallEast(){return hasWallEast;}
    bool getWallSouth(){return hasWallSouth;}
    bool getWallWest(){return hasWallWest;}
    bool getBeenVisited(){return hasBeenVisited;}
    bool getBeenFilled(){return hasBeenFilled;}
    byte getFloodFillValue(){return floodFillValue;}

    void setWallNorth(bool entry){hasWallNorth = entry;}
    void setWallEast(bool entry){hasWallEast = entry;}
    void setWallSouth(bool entry){hasWallSouth = entry;}
    void setWallWest(bool entry){hasWallWest = entry;}
    void setBeenVisited(bool entry){hasBeenVisited = entry;}
    void setBeenFilled(bool entry){hasBeenFilled = entry;}
    void setFloodFillValue(int entry){floodFillValue = entry;}
    

private:
    bool hasWallNorth;
    bool hasWallEast;
    bool hasWallSouth;
    bool hasWallWest;
    bool hasBeenVisited;
    bool hasBeenFilled;
    byte floodFillValue;
};


#endif
