#!/usr/bin/node

const { argv } = require('node:process');
const arg = parseInt(argv[2]);

if (!isNaN(arg)) {
  for (let i = 0; i < arg; i++) {
    let layer = '';
    for (let j = 0; j < arg; j++) {
      layer = layer + '#';
    }
    console.log(layer);
  }
} else {
  console.log('Missing size');
}
