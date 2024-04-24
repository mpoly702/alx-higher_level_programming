#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    // If 'c' is undefined, set it to 'X'
    if (c === undefined) {
      c = 'X';
    }

    // Print the square using the character 'c'
    for (let u = 0; u < this.width; u++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
