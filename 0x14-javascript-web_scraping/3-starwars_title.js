#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = 'http://swapi.co/api/films/' + process.argv[2];
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
