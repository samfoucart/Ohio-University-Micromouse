function FloodFillQueue() {
    this.memory = []
    this.used = 0
    this.front = 0
    this.rear = 0
    this.capacity = 256
    for (var i = 0; i < this.capacity; i++) {
        this.memory.push([0, 0, 0])
    }

    this.pushTriple = (row, collumn, value) => {
        console.log("row: ", row, " collumn: ", collumn, " value: ", value, " used: ", this.used)
        if (this.used < this.capacity) {
            this.memory[this.rear] = [row, collumn, value]
            this.used++
            this.rear = (this.rear + 1) % this.capacity
            return true
        }
        return false
    }

    this.popTriple = () => {
        if (this.used !== 0) {
            this.used--
            tmp = this.front
            this.front = (this.front + 1) % this.capacity
            return this.memory[tmp]
        }
        return [-1, -1, -1]
    }

    this.isEmpty = () => {
        if (this.used === 0) {
            return true
        }

        return false
    }

}