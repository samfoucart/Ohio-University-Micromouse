var sizeUnit
var maze



function setup() {
    createCanvas(windowWidth, windowHeight)
    maze = new Maze()

}

function draw() {

    maze.render()
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}

