#!/usr/bin/node
function factorial (n) {
    // if 'n' is NaN or less than or equal to 0, return 1
    if (Number.isNaN(n) || (n <= 0)) {
      return 1;
    } else {
      // return 'n' multiplied by the factorial of 'n-1'
      return n * factorial(n - 1);
    }
  }
  
  console.log(factorial(Number.parseInt(process.argv[2])));
  