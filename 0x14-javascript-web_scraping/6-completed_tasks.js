#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const request = require('request');
const API_URL: 'https://jsonplaceholder.typicode.com/todos';

request(API_URL, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const dict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dict);
});
