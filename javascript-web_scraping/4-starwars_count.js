#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const requestURL = argv[2];

let countWA = 0;
let completedRequests = 0;

request(requestURL, function (error, response, body) {
  if (error) {
    console.error(`error: ${response.status}`, error);
  } else {
    const bodyData = JSON.parse(body);
    const count = bodyData.count;

    for (let x = 1; x <= count; x++) {
      console.log(`${requestURL}/${x}`);
      request(`${requestURL}/${x}`, function (error, response, body) {
        if (error) {
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
