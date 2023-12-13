function findNaughtyStep(original, modified) {
    // Si la longitud de la original es mayor (Eliminado)
    if(original.length > modified.length){
        for (let i = 0; i < original.length; i++) {
            if(original[i]!=modified[i]){
                return original[i]
            }
        }
    // Si la longitud de la original es menor (Añadido)
    } else if (modified.length > original.length) {
        for (let i = 0; i < modified.length; i++) {
            if(original[i]!=modified[i]){
                return modified[i]
            }
        }
    }       
    return '' // Las cadenas son iguales
  }