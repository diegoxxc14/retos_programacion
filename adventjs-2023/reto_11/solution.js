function getIndexsForPalindrome(word) {
    letters = word.split('')
    lettersRev = word.split('').reverse()
    if (letters.toString()==lettersRev.toString()) {
        return []
    } else {
        let last = letters.length - 1
        let middle = Math.floor(letters.length/2)
        for (let first = 0; first < middle; first++) {

            if(letters[first] != letters[last]) {
                let letter = letters[first]
                console.log(`-first:${first} -last:${last}`)
                console.log(`-first:${letters[first]} -last:${letters[last]}`)

                for (let i = first + 1; i <= last - 1; i++) {
                    letters[first] = letters[i]
                    letters[i] = letter
                    lettersRev = letters
                    console.log('Intercambio : ' + letters.toString())
                    if (letters.toString()==lettersRev.reverse().toString()) {
                        return [first, i]
                    }
                    letters = word.split('')  // Reiniciar
                }
                return null
            }
            last--
        }
    }
  }