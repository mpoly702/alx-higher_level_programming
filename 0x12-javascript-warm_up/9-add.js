#!/usr/bin/node

// Define func 'add' that takes two param. 'a' and 'b' and returns the sum
function add (a, b) {
    return a + b;
  }
  
  console.log(
    add(Number.parseInt(process.argv[2]), Number.parseInt(process.argv[3]))
  );
