function multiplyAll(arr){
    return function mult(mul){
      let myArr = arr.map(x => x*mul)
      return myArr;
    }
  }
console.log(multiplyAll(([1,2,3],1)));