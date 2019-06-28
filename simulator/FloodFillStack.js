import { setMaxListeners } from "cluster";

function FloodFillStack() {
    this.memory = []
    this.top = -1
    for (var i = 0; i < 512; i++) {
        this.memory.push([0, 0, 0])
    }

    this.push = ([row, collumn, value]) => {
        if (self.top >= 512 - 1) {
            return false
        } else {
            self.top++
            self.memory[self.top] = [row, collumn, value]
            return true
        }
    }

    this.pop = () => {
        if (self.top < 0) {
            return
        } else {
            self.top--
            return self.memory[self.top + 1]
        }
    }

    this.isEmpty = () => {
        if (self.top < 0) {
            return true
        } else {
            return false
        }
    }

}