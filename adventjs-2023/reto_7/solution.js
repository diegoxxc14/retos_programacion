function drawGift(size, symbol) {

    if (size==1) return '#\n'

    let spaces = size - 1  // Espacios de la parte superior del cubo
    let edgeUp = size - 2  // Posición de la arista superior del cubo
    let rightSide = 0  // Relleno del lado derecho del cubo
    let faces = symbol.repeat(edgeUp)  // Relleno de las caras del cubo
    let edges = '#'.repeat(size)  // Aristas horizontales
    let res = ' '.repeat(spaces) + edges + '\n'

    for (let i = 0; i < (size * 2) - 3; i++) {
        if(i==edgeUp) {
            res += edges + faces + '#\n'
            rightSide = (rightSide - 1) * -1
            continue
        }
        spaces--
        res += ' '.repeat(spaces<0?0:spaces) + '#' + faces + '#' + symbol.repeat(Math.abs(rightSide)) + '#\n'
        rightSide++
    }
    res += edges + '\n'
    return res
}