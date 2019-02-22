import sys
import API

#mazeValues[][]

def loadWall():
    for i in range(0,16):
        for j in range(0,16):
            if i == 0:
                if j == 0:
                    API.setWall(i, j, "s")
                    API.setWall(i, j, "w")
                elif j == 15:
                    API.setWall(i, j, "n")
                    API.setWall(i, j, "w")
                else:
                    API.setWall(i, j, "w")
            
            if i == 15:
                if j == 0:
                    API.setWall(i, j, "s")
                    API.setWall(i, j, "e")
                elif j == 15:
                    API.setWall(i, j, "n")
                    API.setWall(i, j, "e")
                else:
                    API.setWall(i, j, "e")

            if j == 0 and (i != 0 or i != 15):
                API.setWall(i, j, "s")

            if j == 15 and (i != 0 or i != 15):
                API.setWall(i, j, "n")



def scanWalls():
    for i in range(7,9):
        for j in range(7,9):
            API.setColor(i, j, 'G')
            API.setText(i, j, "0")
    