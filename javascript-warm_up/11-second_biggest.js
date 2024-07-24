#!/usr/bin/node

const { argv } = require('node:process');

function almostMax (argv) {
  /*
   * I have attempted an arrow function here.
   * If it's dumb, well, I tried lol.
   */

  if (argv.length <= 3) {
    return (0);
  }
  let max = 0;
  let secondMax = 0;
  for (let x = 2; argv[x] !== undefined; x++) {
    const arg = () => parseInt(argv[x]);
    if (arg() > secondMax)
    {
      if (arg() > max)
      {
        secondMax = max;
        max = arg();
      } else
      {
        secondMax = arg();
      }
    }
  }
  return (secondMax);
}

console.log(almostMax(argv));
