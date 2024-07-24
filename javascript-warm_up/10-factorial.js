#!/usr/bin/node

const { argv } = require('node:process');

function recursiveFactorial (integer) {
  if (isNaN(integer) || integer <= 1) {
    return (1);
  }
  return integer * recursiveFactorial(integer - 1);
}

console.log(recursiveFactorial(parseInt(argv[2])));
