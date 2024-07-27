#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const requestURL = argv[2];

let countWA = 0;
let completedRequests = 0;

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

    for (let x = 1; x <= count; x++) {
      request(`${requestURL}/${x}`, function (error, response, body) {
        if (error || response.statusCode !== 200) {
          console.error('error: ', error);
        } else {
          const bodyCharacters = (JSON.parse(body).characters);
          if (bodyCharacters.includes('https://swapi-api.hbtn.io/api/people/18/')) {
            countWA++;
          }
        }
        completedRequests++;
        if (completedRequests === count) {
          console.log(countWA);
        }
      });
    }
  }
});
