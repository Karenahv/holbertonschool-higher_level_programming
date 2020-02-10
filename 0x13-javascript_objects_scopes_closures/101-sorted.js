#!/usr/bin/node
// dict

const dict1 = require('./101-data').dict;
const result = {};
for (const k in dict1) {
  if (result[dict1[k]] === undefined) {
    result[dict1[k]] = [];
  }
  result[dict1[k]].push(k);
}
console.log(result);
