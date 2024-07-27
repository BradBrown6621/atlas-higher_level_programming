#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');

request(argv[2], function (error, response, body) {
  if (error) {
    console.error('error: ', error);
  }
  console.log('code:', response && response.statusCode);
});
