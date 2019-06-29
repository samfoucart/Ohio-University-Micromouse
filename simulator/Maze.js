function Maze() {
    this.cellContainer = new Array(256)
    
    // We do two passes through the array to construct every cell,
    // and then to set the outer perimeter.
    for (var i = 0; i < this.cellContainer.length; i++) {
        this.cellContainer[i] = new Cell(i % 16, (i - (i % 16)) / 16 )
    }

    for(var i = 0; i < 16; i++) {
        this.cellContainer[i * 16].setWallLeft(true)
        this.cellContainer[(i * 16) + 15].setWallRight(true)
    }

    for(var j = 0; j < 16; j++) {
        this.cellContainer[j].setWallUp(true)
        this.cellContainer[j + 240].setWallDown(true)
    }

    for(var j = 16; j < 240; j++) {
        var r = random(50)
        if (r < 25) {
            this.cellContainer[j].setWallUp(true)
            this.cellContainer[j - 16].setWallDown(true)
        } else if (r >= 25 && r < 40) {
            this.cellContainer[j].setWallRight(true)
            this.cellContainer[j+1].setWallLeft(true)
        }
    }

    this.cellContainer[119].setValue(0)
    this.cellContainer[120].setValue(0)
    this.cellContainer[135].setValue(0)
    this.cellContainer[136].setValue(0)

    this.render = () => {
        for (var i = 0; i < 256; i++) {
            this.cellContainer[i].render()
        }
    }

    this.getCoordinatesFromIndex = (index) => {
        return [index % 16, (index - (index % 16)) / 16]
    }

    this.getCell = (row, collumn) => {
        return this.cellContainer[(row * 16) + collumn]
    }

    this.floodFill = (row, collumn) => {
        queue = new FloodFillQueue()
        value = 0
        cell = this.cellContainer[(row * 16) + collumn]
        cell.setValue(value)
        queue.pushTriple(row, collumn, value)
        while (!queue.isEmpty()) {
            [row, collumn, value] = queue.popTriple()
            cell = this.cellContainer[(row * 16) + collumn]
            cell.setValue(value)

            if(!cell.getWallUp()) {
                other = this.cellContainer[((row - 1) * 16) + collumn].getValue()
                if (other > value || other === -1) {
                    queue.pushTriple(row - 1, collumn, value + 1)
                }
            }

            if(!cell.getWallRight()) {
                other = this.cellContainer[(row * 16) + collumn + 1].getValue()
                if (other > value || other === -1) {
                    queue.pushTriple(row, collumn + 1, value + 1)
                }
            }

            if(!cell.getWallDown()) {
                other = this.cellContainer[((row + 1) * 16) + collumn].getValue()
                if (other > value || other === -1) {
                    queue.pushTriple(row + 1, collumn, value + 1)
                }
            }
            
            if(!cell.getWallLeft()) {
                other = this.cellContainer[(row * 16) + collumn - 1].getValue()
                if (other > value || other === -1) {
                    queue.pushTriple(row, collumn - 1, value + 1)
                }
            } 
        }
    }

    this.turnTowardsBest = (mouse) => {
        row = mouse.getRow()
        collumn = mouse.getCollumn()
        direction = mouse.getDirection()
        cell = this.cellContainer[(row * 16) + collumn]
        currentValue = cell.getValue()
        values = []

        if (!cell.getWallRight()) {
            other = this.cellContainer[(row * 16) + collumn + 1].getValue()
            if (other < currentValue && other !== -1) {
                values.push(other)
            } else {
                values.push(255)
            }
        } else {
            values.push(255)
        }

        if (!cell.getWallDown()) {
            other = this.cellContainer[((row + 1) * 16) + collumn].getValue()
            if (other < currentValue && other !== -1) {
                values.push(other)
            } else {
                values.push(255)
            }
        } else {
            values.push(255)
        }

        if (!cell.getWallLeft()) {
            other = this.cellContainer[(row * 16) + collumn - 1].getValue()
            if (other < currentValue && other !== -1) {
                values.push(other)
            } else {
                values.push(255)
            }
        } else {
            values.push(255)
        }

        if (!cell.getWallUp()) {
            other = this.cellContainer[((row - 1) * 16) + collumn].getValue()
            if (other < currentValue && other !== -1) {
                values.push(other)
            } else {
                values.push(255)
            }
        } else {
            values.push(255)
        }

        console.log("values: ", values)
        bestDir = direction
        lowestNeighbor = 255
        for (var i = 0; i < 4; i++) {
            if (lowestNeighbor > values[(direction + i) % 4]){
                bestDir = (direction + i) % 4
                lowestNeighbor = values[(direction + i) % 4]
            }
        }
        if (lowestNeighbor === 255) {
            console.log("Mouse is Stuck")
            return false
        }


        switch (direction) {
            case 0:
                switch (bestDir) {
                    case 0:
                        return true
                    case 1:
                        mouse.turnRight()
                        return true
                    case 2:
                        mouse.turnRight()
                        mouse.turnRight()
                        return true
                    case 3:
                        mouse.turnLeft()
                        return true
                    default:
                        return false
                }
            case 1:
                switch (bestDir) {
                    case 0:
                        mouse.turnLeft()
                        return true
                    case 1:
                        return true
                    case 2:
                        mouse.turnRight()
                        return true
                    case 3:
                        mouse.turnRight()
                        mouse.turnRight()
                        return true
                    default:
                        return false
                }
            case 2:
                switch (bestDir) {
                    case 0:
                        mouse.turnRight()
                        mouse.turnRight()
                        return true
                    case 1:
                        mouse.turnLeft()
                        return true
                    case 2:
                        return true
                    case 3:
                        mouse.turnRight()
                        return true
                    default:
                        return false
                }
            case 3:
                switch (bestDir) {
                    case 0:
                        mouse.turnRight()
                        return true
                    case 1:
                        mouse.turnRight()
                        mouse.turnRight()
                        return true
                    case 2:
                        mouse.turnLeft()
                        return true
                    case 3:
                        return true
                    default:
                        return false
                }
        }
    }
}