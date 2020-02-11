#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = 'http://swapi.co/api/films/' + process.argv[2];
const myRequest2 = require('request');
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const jsonBody = JSON.parse(body).characters;
    for (const j in jsonBody) {
      const chars = jsonBody[j];
      myRequest2(chars, function (err, res, body2) {
        if (err) {
          console.log(err);
        } else {
          const actor = JSON.parse(body2).name;
          console.log(actor);
        }
      });
    }
  }
});
