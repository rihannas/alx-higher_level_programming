#!/usr/bin/node
let j = process.argv[2]
let i = 0
if (isNaN(j)) {
    console.log('Missing number of occurrences')
} else {
for (i; i < j; i++) {
    console.log('c is cool');
}
}


// if (isNaN(process.argv[2]) || (process.argv[2] === undefined)) {
//   console.log('Missing number of occurrences');
// } else {
//   let i = 0;
//   const x = Number(process.argv[2]);
//   for (i; i < x; i++) {
//     console.log('C is fun');
//   }
// }
