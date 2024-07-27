#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('node:fs');

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
