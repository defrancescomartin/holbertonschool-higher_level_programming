#!/usr/bin/node
module.exports = class Rectangle {
  constructor (width, height) {
    this.width = width;
    this.height = height;
    if (!width || !height || width <= 0 || height <= 0) {
      return (Rectangle);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
