#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
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
}

module.exports = Square;
