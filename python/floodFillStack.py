import sys
import API
import cell

MAXSIZE = 512

class floodFillStack:
    def __init__(self):
        self.top = -1
        for i in range(0,512):
            self.memory = [cell.Cell()]

    def push(self, currentCell):
        if self.top >= MAXSIZE - 1:
            sys.stderr.write("Stack Overflow \n")
            return False
        else:
            self.top += 1
            self.memory[self.top] = currentCell
            return True

    def pop(self):
        if self.top < 0:
            sys.stderr.write("Stack Underflow \n")
            return
        else:
            popCell = self.memory[self.top]
            self.top -= 1
            return popCell
        return

    def isEmpty(self):
        if self.top < 0:
            return True
        else:
            return False

