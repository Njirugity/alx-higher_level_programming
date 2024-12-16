#!/usr/bin/node

function add (a, b) {
  return a + b;
}

if (isNaN(process.argv[2]) || process.argv[2] === undefined || process.argv[3] ===
  undefined) {
  console.log('NaN');
} else {
  const x = Number(process.argv[2]);
  const y = Number(process.argv[3]);

  console.log(add(x, y));
}
