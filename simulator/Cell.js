function Cell(row, collumn, wallUp = false, wallRight = false, wallDown = false, wallLeft = false, color = 200) {
    // 16x16 Position Coordinate
    // 0x0 would be top left cell, while 16x16 is bottom right
    this.xPosition = row
    this.yPosition = collumn
    //console.log("Loading: (", this.xPosition, ", ", this.yPosition, ")")

    // Wall Booleans
    this.wallLeft = wallLeft
    this.wallRight = wallRight
    this.wallUp = wallUp
    this.wallDown = wallDown

    // color only for drawing purposes
    this.color = color

    // margin and scale so that screen looks good on multiple resolutions
    this.margin = screen.width * .01
    this.scale = screen.height * .04

    this.floodFillValue = -1

    this.getValue = () => {
        return this.floodFillValue
    }

    this.setValue = (value) => {
        this.floodFillValue = value
    }

    // Getters and Setters
    this.setWallLeft = (wallLeft) => {
        this.wallLeft = wallLeft
    }

    this.setWallDown = (wallDown) => {
        this.wallDown = wallDown
    }

    this.setWallUp = (wallUp) => {
        this.wallUp = wallUp
    }
    
    this.setWallRight = (wallRight) => {
        this.wallRight = wallRight
    }

    this.getWallRight = () => {
        return this.wallRight
    }

    this.getWallDown = () => {
        return this.wallDown
    }

    this.getWallLeft = () => {
        return this.wallLeft
    }

    this.getWallUp = () => {
        return this.wallUp
    }

    // Render
    this.render = () => {
        //this.scale = windowHeight
        push()
        fill(this.color)
        noStroke()
        rect((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin, this.scale, this.scale)

        beginShape(LINES)
        stroke('red')
        strokeWeight(2)
        if (this.wallUp) {
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin)
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin)
        }
        if (this.wallRight) {
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin)
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin + this.scale)
        }
        if (this.wallDown) {
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin + this.scale)
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin + this.scale)
        }
        if (this.wallLeft) {
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin + this.scale)
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin)
        }
        endShape()

        beginShape(LINES)
        stroke(175)
        strokeWeight(2)
        if (!this.wallUp) {
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin)
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin)
        }
        if (!this.wallRight) {
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin)
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin + this.scale)
        }
        if (!this.wallDown) {
            vertex((this.xPosition * this.scale) + this.margin + this.scale, (this.yPosition * this.scale) + this.margin + this.scale)
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin + this.scale)
        }
        if (!this.wallLeft) {
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin + this.scale)
            vertex((this.xPosition * this.scale) + this.margin, (this.yPosition * this.scale) + this.margin)
        }
        endShape()

        fill(0, 0, 0)
        text(this.floodFillValue, (this.xPosition * this.scale) + this.margin + (this.scale / 2), (this.yPosition * this.scale) + this.margin + (this.scale / 2))
        textAlign(CENTER)
        
        pop()
    }

    
}