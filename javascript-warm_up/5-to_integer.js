#!/usr/bin/node

const { argv } = require('node:process');
const argInt = parseInt(argv[2]);

if (isNaN(argInt)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argInt}`);
}
