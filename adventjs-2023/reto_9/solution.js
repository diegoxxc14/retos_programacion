function adjustLights(lights) {
    let l1 = '🔴', l2 = '🟢'
    let op1 = 0, op2 = 0
    for (let i = 0; i < lights.length; i++) {
        const elm = lights[i]
        
        if (i%2==0) {  // Luces pares (1ra combinación)
            if (elm!=l1) op1++  // Si la luz es diferente '🔴'
            else if (elm!=l2) op2++  // Sino, es diferente '🟢'
        } else {  // Luces impares (2da combinación)
            if (elm!=l2) op1++  // Si la luz es diferente '🟢'
            else if (elm!=l1) op2++  // Sino, es diferente '🔴'
        }
    }

    // Devolver el mínimo de cambios de las 2 combinaciones
    return Math.min(op1, op2)
}