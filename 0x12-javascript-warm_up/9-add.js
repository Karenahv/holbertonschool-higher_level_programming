#!/usr/bin/node

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return a + b;
}
console.log(add(process.argv[2], process.argv[3]));
