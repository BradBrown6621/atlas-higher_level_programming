#!/usr/bin/node

const { argv } = require('node:process');

const args = argv.slice(2);

const a = args[0];
const b = args[1];

console.log(`${a} is ${b}`);
