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
}