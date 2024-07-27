#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const requestURL = argv[2];

let countWA = 0;

request(requestURL, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error(`error: ${response.status}`, error);
  } else {
    let bodyData;
    try {
      bodyData = JSON.parse(body);
    } catch (e) {
      console.log('0');
      return;
    }
    const count = bodyData.count;

    for (let x = 0; x < count; x++) {
      const result = bodyData.results[x];
      if (result.characters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
        countWA++;
      }
    }
    console.log(countWA);
  }
});
