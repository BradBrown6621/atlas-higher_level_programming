#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.size; y++) {
      let layer = [];
      for (let x = 0; x < this.size; x++) {
        layer += c;
      }
      console.log(layer);
    }
  }

  double () {
    super.double(this.size);
    this.size *= 2;
  }
}

module.exports = Square;
