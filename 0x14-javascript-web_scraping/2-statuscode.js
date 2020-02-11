#!/usr/bin/node
// status of a request
const myRequest = require('request');
myRequest.get(process.argv[2], function (err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
