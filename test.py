import API
import sys
import mmLib

def log(string):
    sys.stderr.write("{}\n".format(string))

def main():
    mmLib.loadWall()
    mmLib.scanWalls()

if __name__ == "__main__":
    main()