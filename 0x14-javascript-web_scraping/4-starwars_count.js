#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = process.argv[2];
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const jsonBody = JSON.parse(body).results;
    for (let i = 0; i < jsonBody.length; i++) {
      const chars = jsonBody[i].characters;
      for (let j = 0; j < chars.length; j++) {
        if (chars[j].search('/18/') > 0) {
          count = count + 1;
        }
      }
    }
    console.log(count);
  }
});
