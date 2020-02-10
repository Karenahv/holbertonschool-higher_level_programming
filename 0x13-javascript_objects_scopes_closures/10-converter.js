#!/usr/bin/node
// converter

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
