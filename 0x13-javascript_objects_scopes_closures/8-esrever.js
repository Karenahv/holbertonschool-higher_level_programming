#!/usr/bin/node
// reverse a list

exports.esrever = function (list) {
  const reverse = [];
  for (let i = list.length; i-- > 0;) {
    reverse.push(list[i]);
  }
  return reverse;
};
