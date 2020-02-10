#!/usr/bin/node
// map

const data = require('./100-data').list;
console.log(data);
console.log(data.map((x, index) => x * index));
