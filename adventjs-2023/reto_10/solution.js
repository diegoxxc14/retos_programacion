function createChristmasTree(ornaments, height) {
    let spaces = height - 1  // Espacios en blanco a la izquierda
    let iOrn = 0  // Posición del adorno a colgar
    let branch = ''  // Rama del árbol
    let res = ''
    for (let i = 0; i < height; i++) {  // Altura del árbol
        for (let j = 0; j < i + 1; j++) {  // Adornos en la rama
            if (iOrn==ornaments.length) iOrn=0
            branch += ornaments[iOrn] + ' '
            iOrn++
        }
        res += ' '.repeat(spaces) + branch.trimEnd() + '\n'
        branch = ''
        spaces--
    }
    return res + ' '.repeat(height - 1) + '|\n'
}