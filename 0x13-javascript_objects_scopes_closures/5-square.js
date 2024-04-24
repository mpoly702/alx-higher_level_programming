#!/usr/bin/node

// Import the Rectangle class
const Rectangle = require('./4-rectangle');

// class name Square inherits from Rectangle
class Square extends Rectangle {
  constructor (size) {
    // Call the constructor with width and height set to 'size'
    super(size, size);
  }
}

// Export the Square class for use in other modules
module.exports = Square;
