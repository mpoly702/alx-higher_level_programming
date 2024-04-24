#!/usr/bin/node

// Convert the 1st cmd line arg to an int
const n = Number.parseInt(process.argv[2]);

// Check if the converted value is NaN
console.log(Number.isNaN(n) ? 'Not a number' : 'My number: ' + n);
