#!/usr/bin/node

const len = process.argv.length;

if (len <= 3) {
  console.log(0);
} else {
  let maxOne = 0;
  let maxTwo = 0;
  for (let i = 2; i < len; i++) {
    if (Number(process.argv[i]) > maxOne) {
      maxTwo = maxOne;
      maxOne = Number(process.argv[i]);
    } else if (Number(process.argv[i]) > maxTwo && Number(process.argv[i]) !== maxOne) {
      maxTwo = Number(process.argv[i]);
    }
  }
  console.log(maxTwo);
}
