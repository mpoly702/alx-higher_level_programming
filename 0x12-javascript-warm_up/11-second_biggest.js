#!/usr/bin/node

// Check if there are less than or equal to 3 cmd line arg
if (process.argv.length <= 3) {
    console.log('0');
  } else {
    // Extract numeric values from cmd line arg
    const ar = process.argv.slice(2).map(Number);
    // Sort the arr of num in descending order and retrieve the nxt largest num
    const next = ar.sort(function (a, b) { return b - a; })[1];
    console.log(next);
  }
