#!/usr/bin/node
let max = 0;
let max2 = 0;
const len = process.argv.length;
if (len <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (parseInt(process.argv[i]) > max) {
      max = process.argv[i];
    }
  }
  for (let j = 2; j < len; j++) {
    if (parseInt(process.argv[j]) < max && parseInt(process.argv[j]) > max2) {
      max2 = process.argv[j];
    }
  }
  console.log(max2);
}
