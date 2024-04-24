#!/usr/bin/node

// Check if the 1st cmd line arg is undefined or not a num
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing size');
  } else {
    // If the argument is a valid number
    const v = Number(process.argv[2]);
    let u = 0;
  
    // Loop through each row of the square
    while (u < v) {
      console.log('X'.repeat(v));
      u++;
    }
  }
