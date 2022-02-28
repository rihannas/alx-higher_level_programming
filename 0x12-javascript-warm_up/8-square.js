#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
}

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i;
  let j;
  const x = Number(process.argv[2]);
  let sqr = '';

  for (i = 0; i < x; i++) {
    for (j = 0; j < x; j++) {
      sqr += 'X';
    }
    sqr += '\n';
  }
  console.log(sqr);
}
