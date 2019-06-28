function Mouse() {
    this.row = 0
    this.collumn = 0
    this.direction = 0

    // margin and scale so that screen looks good on multiple resolutions
    this.margin = screen.width * .01
    this.scale = screen.height * .04

    this.xVertices = [
        (this.collumn * this.scale) + this.margin + (this.scale * .2),
        (this.collumn * this.scale) + this.margin + (this.scale * .8),
        (this.collumn * this.scale) + this.margin + (this.scale * .9),
        (this.collumn * this.scale) + this.margin + (this.scale * .8),
        (this.collumn * this.scale) + this.margin + (this.scale * .2)
    ]

    this.yVertices = [
        (this.row * this.scale) + this.margin + (this.scale * .2),
        (this.row * this.scale) + this.margin + (this.scale * .2),
        (this.row * this.scale) + this.margin + (this.scale * .5),
        (this.row * this.scale) + this.margin + (this.scale * .8),
        (this.row * this.scale) + this.margin + (this.scale * .8)
    ]

    this.turnRight = () => {
        this.direction = (this.direction + 1) % 4
    }

    this.turnLeft = () => {
        this.direction = (this.direction + 3) % 4
    }

    this.moveForward = (cell) => {
        if (this.direction === 0 && !cell.getWallRight()) {
            this.collumn++
        } else if (this.direction === 1 && !cell.getWallDown()) {
            this.row++
        } else if (this.direction === 2 && !cell.getWallLeft()) {
            this.collumn--
        } else if (this.direction === 3 && !cell.getWallUp()) {
            this.row--
        }
    }
    

    this.render = function() {
        push()
        
        
        translate((this.collumn * this.scale) + this.margin + (this.scale / 2), (this.row * this.scale) + this.margin + (this.scale / 2))
        rotate(this.direction * HALF_PI)
        triangle(-this.scale * .2, this.scale * .2, -this.scale * .2, -this.scale * .2, this.scale * .2, 0)
        
        pop()
    }

    this.getRow = () => {
        return this.row
    }

    this.getCollumn = () => {
        return this.collumn
    }

    this.getDirection = () => {
        return this.direction
    }


}