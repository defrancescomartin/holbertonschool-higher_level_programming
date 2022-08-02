#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    let i = 0;
    for (i; i < this.widht; i++) { console.log(c.repeat(this.height)); }
  }
};
