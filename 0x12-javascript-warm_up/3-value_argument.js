#!/usr/bin/node

// Retrieve the first cmd line arg
const ar = process.argv[2];

// Check if the argument is defined
console.log(ar !== undefined ? ar : 'No argument');
