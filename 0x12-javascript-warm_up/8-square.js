#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  for (let i = 0; i < x; i++) {
    let result = '';
    for (let j = 0; j < x; j++) {
      result += 'X';
    }
    console.log(result);
  }
}
