#!/usr/bin/node

class Rectangle {
    constructor (w, h) {
      // Check if both width and height are greater than 0
      if (w > 0 && h > 0) {
        // If true, initialize the width and height attributes
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      // Loop through each row
      for (let i = 0; i < this.height; i++) {
        // Print 'X' char to create a row
        console.log('X'.repeat(this.width));
      }
    }
  }
  
  module.exports = Rectangle;
