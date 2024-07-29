#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

function addToDict (dict, key, value) {
  if (dict) {
    if (Object.prototype.hasOwnProperty.call(dict, key)) {
      dict[`${key}`] += value;
    } else {
      dict[`${key}`] = value;
    }
  }
}

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.completed === true) {
        addToDict(dict, task.userId, 1);
      }
    }
    console.log(dict);
  }
});
