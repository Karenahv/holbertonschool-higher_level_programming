#!/usr/bin/node
// copy content of a web in a file
const myRequest = require('request');
const myUrl = process.argv[2];
const fs = require('fs');
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
