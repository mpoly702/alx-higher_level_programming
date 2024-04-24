#!/usr/bin/node

let numarg = 0;

exports.logMe = function (item) {
  // Print the number of arguments/new argument value
  console.log(numarg + ': ' + item);

  numarg++;
};
