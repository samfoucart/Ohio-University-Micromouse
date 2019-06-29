var sizeUnit
var maze
var mouse
var playing = false



function setup() {
    frameRate(5)
    createCanvas(windowWidth - (windowWidth / 32), windowHeight - (windowWidth / 32))
    maze = new Maze()
    mouse = new Mouse()
    maze.floodFill(7, 8)
    maze.floodFill(7, 7)
    maze.floodFill(8, 7)
    maze.floodFill(8, 8)

}

function draw() {

    maze.render()
    mouse.render()
    if (playing) {
        if (maze.turnTowardsBest(mouse)) {
            mouse.render()
            mouse.moveForward(maze.getCell(mouse.getRow(), mouse.getCollumn()))
            mouse.render()
        } 
    }
    
}

function windowResized() {
    resizeCanvas(windowWidth - (windowWidth / 32), windowHeight - (windowWidth / 32))
}

function keyPressed() {
    switch (keyCode) {
        case RIGHT_ARROW:
            mouse.turnRight()
            break
        case LEFT_ARROW:
            mouse.turnLeft()
            break
        case UP_ARROW:
            playing = true
            break
        default:
            break
    }
}

