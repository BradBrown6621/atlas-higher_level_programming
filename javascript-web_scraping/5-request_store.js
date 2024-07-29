#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');
const request = require('request');

const url = argv[2];
const file = argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else if (response) {
    fs.writeFile(file, body, 'utf8', (err, data) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
