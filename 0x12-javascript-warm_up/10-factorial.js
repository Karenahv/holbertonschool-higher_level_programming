#!/usr/bin/node

function factorial (a) {
  a = parseInt(a);
  if (!isNaN(a)) {
    if (a !== 1) {
      const f = a * factorial(a - 1);
      return f;
    } else {
      return 1;
    }
  } else {
    return 1;
  }
}
console.log(factorial(process.argv[2]));
