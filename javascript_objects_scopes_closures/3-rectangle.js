#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      let layer = [];
      for (let x = 0; x < this.width; x++) {
        layer += 'X';
      }
      console.log(layer);
    }
  }
}

module.exports = Rectangle;
