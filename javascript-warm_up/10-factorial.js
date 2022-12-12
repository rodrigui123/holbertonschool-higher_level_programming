#!/usr/bin/node

function factorial(n) {
    // If n is 0 or 1, the factorial is 1
    if (n <= 1) {
      return 1;
    }
    return n * factorial(n - 1);
  }
  let n = parseInt(process.argv[2]);
  let result = factorial(n);
  console.log(result);
