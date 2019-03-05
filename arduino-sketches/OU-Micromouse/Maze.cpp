#include "Maze.h"
#include "arduino.h"
/*
Maze::Maze()
{
  for (Cell::byte i = 0; i < 16; ++i)
  {
    for (Cell::byte j = 0; j < 16; ++j)
    {
      data[i][j] = Cell();
    }
  }
}
*/


Maze::Maze()
{
    for (Cell::byte i = 0; i < 16; ++i)
    {
        for (Cell::byte j = 0; j < 16; ++j)
        {
            Cell * cellPtr;
            cellPtr = new Cell;
            data[i][j] = cellPtr;
        }
    }

    mousePosition = 0;
    mouseDirection = 0;
}

Maze::~Maze()
{
    for (Cell::byte i = 0; i < 16; ++i)
    {
        for (Cell::byte j = 0; j < 16; ++j)
        {
            delete data[i][j];
            data[i][j] = nullptr;
        }
    }
}


void Maze::initializePerimiter()
{
    for (Cell::byte i = 0; i < 16; ++i)
    {
        for(Cell::byte j = 0; j < 16; ++j)
        {
            if (i == 0)
                data[i][j]->setWallSouth(true);
            
            if (i == 15)
                data[i][j]->setWallNorth(true);

            if (j == 0)
                data[i][j]->setWallWest(true);

            if (j == 15)
                data[i][j]->setWallEast(true);

        }
    }
}

void Maze::initializeCenter()
{
    for (Cell::byte i = 0; i < 16; ++i)
    {
        for (Cell::byte j = 0; j < 16; ++j)
        {
            data[i][j]->setFloodFillValue(-1);
            if ((i == 7 || i == 8) && (j == 7 || j == 8))
                data[i][j]->setFloodFillValue(0);
            
        }
    }
}

void Maze::printFlood()
{
    for (Cell::byte i = 0; i < 16; ++i)
    {
        Serial.print("----");
    }
    Serial.print('\n');

    for (Cell::byte i = 15; i >= 0; --i)
    {
        for (Cell::byte j = 0; j < 16; ++j)
        {
            if (j == 0)
                Serial.print('|');

            Serial.print("    ");
            Serial.print(data[i][j]->getFloodFillValue());
            Serial.print('|');
            if (j == 15)
                Serial.print('\n');
        }
    }

    for (Cell::byte i = 0; i < 16; ++i)
    {
        Serial.print("----");
    }
    Serial.print('\n');
}

void Maze::floodFill(int x, int y)
{
    // Look Up
    if (data[y][x]->getWallNorth() == false)
    {
        if (data[y+1][x]->getFloodFillValue() > data[y][x]->getFloodFillValue() || data[y+1][x]->getFloodFillValue() == -1)
        {
            data[y+1][x]->setFloodFillValue(data[y][x]->getFloodFillValue() + 1);
            floodFill(x, y + 1);
        }
    }

    // Look Down
    if (data[y][x]->getWallSouth() == false)
    {
        if (data[y-1][x]->getFloodFillValue() > data[y][x]->getFloodFillValue() || data[y-1][x]->getFloodFillValue() == -1)
        {
            data[y-1][x]->setFloodFillValue(data[y][x]->getFloodFillValue() + 1);
            floodFill(x, y - 1);
        }
    }
    
    // Look Right
    if (data[y][x]->getWallEast() == false)
    {
        if (data[y][x+1]->getFloodFillValue() > data[y][x]->getFloodFillValue() || data[y][x+1]->getFloodFillValue() == -1)
        {
            data[y][x+1]->setFloodFillValue(data[y][x]->getFloodFillValue() + 1);
            floodFill(x + 1, y);
        }
    }

    // Look Left
    if (data[y][x]->getWallWest() == false)
    {
        if (data[y][x-1]->getFloodFillValue() > data[y][x]->getFloodFillValue() || data[y][x-1]->getFloodFillValue() == -1)
        {
            data[y][x-1]->setFloodFillValue(data[y][x]->getFloodFillValue() + 1);
            floodFill(x - 1, y);
        }
    }

    Serial.print('(');
    Serial.print(x);
    Serial.print(", ");
    Serial.print(y);
    Serial.print(")\n");
    return;
}

void Maze::floodFillCenter()
{
    for (int i = 7; i < 9; ++i)
        for (int j = 7; j < 9; ++j)
            floodFill(j,i);
    
}
