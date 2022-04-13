#!/usr/bin/node
//  script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const episode = process.argv[2];
const api_URL = 'https://swapi-api.hbtn.io/api/films/';

resquest(api_URL + episode, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
