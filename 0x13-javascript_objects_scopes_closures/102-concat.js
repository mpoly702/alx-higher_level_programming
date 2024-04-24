#!/usr/bin/node

const firstFile = process.argv[2];
const secondFile = process.argv[3];
const thirdFile = process.argv[4];

// Import the file system module
const fs = require('fs');

// Read the content of the first/second source file
const contentA = fs.readFileSync(firstFile, 'utf8');
const contentB = fs.readFileSync(secondFile, 'utf8');

// Concatenate the contents of both files
const concatenatedText = contentA + contentB;

fs.writeFileSync(thirdFile, concatenatedText);
