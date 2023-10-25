#!/usr/bin/node

let sliced = process.argv.slice(2)
if (sliced.length < 2) {
    console.log(0)
} else {
    let largestNumber = Math.max(...sliced);
    sliced.pop(largestNumber)
    largestNumber = Math.max(...sliced);
    console.log(largestNumber)
}


// if (process.argv.length <= 3) {
//   console.log('0');
// } else {
//   const arr = process.argv.slice(2).map(Number);
//   const second = arr.sort(function (a, b) { return b - a; })[1];
//   console.log(second);
// }
