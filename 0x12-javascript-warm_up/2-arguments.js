#!/usr/bin/node
let n;
if (process.argv.length <= 2) {
  n = 'No argument';
} else if (process.argv.length === 3) {
  n = 'Argument found';
} else {
  n = 'Arguments found';
}
console.log(n);
