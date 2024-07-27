#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[2]}`, function (error, response, body) {
  if (error) {
    console.error('error: ', error);
  } else {
    const bodyData = JSON.parse(body);
    console.log(bodyData.title);
  }
});
