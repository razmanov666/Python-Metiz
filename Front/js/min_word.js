function findShort(s){
    let str = s.split(' '), arr = [];
    str.forEach(x => {if (x.length != 0 && isNaN(x.length) != true) arr.push(x.length)});
    let min = Math.min.apply(null, arr);
    return min;
  }
  console.log(findShort('a s ss'));