var sizeUnit
var maze
var mouse



function setup() {
    createCanvas(windowWidth - (windowWidth / 32), windowHeight - (windowWidth / 32))
    maze = new Maze()
    mouse = new Mouse()

}

function draw() {

    maze.render()
    mouse.render()
    
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
            mouse.moveForward(maze.getCell(mouse.getRow(), mouse.getCollumn()))
            break
        default:
            break
    }
}

