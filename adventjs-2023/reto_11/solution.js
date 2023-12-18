function getIndexsForPalindrome(word) {
    let letters = word.split('')
    let lettersRev = word.split('').reverse()
    let last = letters.length - 1
    let middle = Math.floor(letters.length/2)
    for (let first = 0; first <= middle; first++) {
        if(letters[first] != letters[last]) {
            let letterFirst = letters[first]
            for (let i = first + 1; i <= middle; i++) {
                letters[first] = letters[i]
                letters[i] = letterFirst
                lettersRev = letters
                if (letters.toString()==lettersRev.reverse().toString()) {
                    return [first, i]
                }
                letters = word.split('')  // Reiniciar
            }
            let letterLast = letters[last]
            for (let i = last; i >= middle; i--) {
                letters[last] = letters[i]
                letters[i] = letterLast
                lettersRev = letters
                if (letters.toString()==lettersRev.reverse().toString()) {
                    return [i, last]
                }
                letters = word.split('')  // Reiniciar
            }
            return null
        }
        last--
    }
    return []
  }