#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  const x = Number(process.argv[2]);
  while (count < x) {
    console.log('C is fun');
    count++;
  }
}
