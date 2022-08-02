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

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
