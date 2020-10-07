function squareDigits(num){
    myNum = num.toString(10);
    return +(Array.from(myNum, x => x * x).join(''));
  }
console.log(squareDigits(141));