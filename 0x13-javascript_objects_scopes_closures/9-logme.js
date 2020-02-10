#!/usr/bin/node
// number arguments
let numargs = 0;
exports.logMe = function (item) {
  console.log(`${numargs}: ${item}`);
  numargs = numargs + 1;
};
