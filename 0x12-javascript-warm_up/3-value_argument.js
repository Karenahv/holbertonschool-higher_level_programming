#!/usr/bin/node
let n;
if (process.argv.length <= 2) {
  n = 'No argument';
} else if (process.argv.length === 3) {
  n = process.argv[2];
} else {
  n = process.argv[2];
}
console.log(n);
