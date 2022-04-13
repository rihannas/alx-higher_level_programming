#!/usr/bin/node
// a script that display the status code of a GET request.

const request = require('request');
const URL = process.argv[2];

resquest(URL, function (error, response) {
  if (error) {
    console.error(error);
  }
  console.log('code: ' + response.statusCode);
});
