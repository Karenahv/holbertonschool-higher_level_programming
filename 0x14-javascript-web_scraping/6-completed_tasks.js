#!/usr/bin/node
// status of a request
const myRequest = require('request');
const myUrl = process.argv[2];
myRequest(myUrl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const dict1 = {};
    const jsonBody = JSON.parse(body);
    if (jsonBody != null) {
      let userant = jsonBody[0].userId;
      for (let j = 1; j < jsonBody.length; j++) {
        for (let i = 0; i < jsonBody.length; i++) {
          const user = jsonBody[i].userId;
          if (jsonBody[i].completed === true && userant === user) {
            count = count + 1;
            dict1[jsonBody[i].userId] = count;
          }
        }
        userant = jsonBody[j].userId;
        count = 0;
      }
    }
    console.log(dict1);
  }
});
