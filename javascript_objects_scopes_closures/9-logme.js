#!/usr/bin/node

let numLogs = 0;

exports.logMe = function (item) {
  console.log(`${numLogs}: ${item}`);
  numLogs++;
};
