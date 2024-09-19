function findComplement(num) {

  const binaryStr = num.toString(2);


  let complementStr = '';

  
  for (let i = 0; i < binaryStr.length; i++) {

    complementStr += binaryStr[i] === '0' ? '1' : '0';
  }

  
  return parseInt(complementStr, 2);
}

const num = 5;
const complement = findComplement(num);
console.log(complement); // Output: 2