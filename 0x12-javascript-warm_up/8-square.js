#!/usr/bin/node

let size = process.argv[2]

if (isNaN(size)) {
    console.log('Missing size')
} else {
for (let i = 0; i < size; i++) {
    row = ''
    for (let j = 0; j < size; j++) {
    row += 'X'
    }
    console.log(row)
}
}

// if (isNaN(process.argv[2])) {
//   console.log('Missing size');
// } else if (process.argv[2] === undefined) {
//   console.log('Missing size');
// } else {
//   let i = 0;
//   const x = Number(process.argv[2]);

//   while (i < x) {
//     console.log('X'.repeat(x));
//     i++;
//   }
// }
