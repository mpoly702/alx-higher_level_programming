#!/usr/bin/node

// Check if the 1st cmd line arg is undefined or not a num
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
    console.log('Missing number of occurrences');
  } else {
    // If the argument is a valid number
    const v = Number(process.argv[2]);
    let u = 0;
  
    // Loop while u is less than the specified number of occurrences
    while (u < v) {
      console.log('C is fun');
      u++;
    }
  }
