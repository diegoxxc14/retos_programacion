function manufacture(gifts, materials) {
    var res=[]
    for (let g of gifts) {
        res.push(g)  // Agregamos el regalo
        for (let i = 0; i < g.length; i++) {
            if(!materials.includes(g[i])) {  // Si no incluye un material lo elinamos
                res.pop()
                break
            }
        }
  }
  return res
}