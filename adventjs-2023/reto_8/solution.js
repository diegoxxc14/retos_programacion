function organizeGifts(gifts) {
  let res = ''
    while(gifts!=''){
      let iGift = gifts.search('[a-z]')  // Posición del regalo
      let gift = gifts[iGift]  // Obtener el regalo
      let amount = parseInt(gifts.split(gift)[0])  // Total de regalos
      let numBoxes = Math.floor(amount/10)  // Calcular total de cajas
      let numPallets = Math.floor(numBoxes/5)  // Calcular toral palés
      let leftover = 0  // Total sobrantes

      // Ordenar palés, si existen
      if (numPallets > 0) res += `[${gift}]`.repeat(numPallets)

      // Ordenar cajas, si hay
      res += `{${gift}}`.repeat(numBoxes - (numPallets * 5))

      // Ordenar sobrantes si existen
      leftover = amount%10
      if(leftover > 0) res+=`(${gift.repeat(leftover)})`
      
      gifts = gifts.substr(iGift + 1)  // Actualizar la cadena de regalos
    }
    return res
  }