function count (string) {
  let tempI, tempJ, count = 0;
  let arr = new Array ;
  let myString = string.split('');
  if (string.isEmpty){
  return {};}
  else {
    for (let i = 0; i < myString.length; i++){
      tempI = myString[i];
        for (let j = 0; j < myString.length; j++){
          tempJ = myString[j];
          if (tempI == tempJ) count++;
        }
      arr.set(myString[i], count)
   }
  }
}
console.log(count('avs'));