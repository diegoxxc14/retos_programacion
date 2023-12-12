function findFirstRepeated(gifts) {
    let aux = new Set()
        for (let gift of gifts) {
            if(aux.has(gift))
                return gift
            aux.add(gift)
        }
    return -1
}