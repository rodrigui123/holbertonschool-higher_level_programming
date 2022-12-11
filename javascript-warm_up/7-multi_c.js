#!/usr/bin/node

const x = process.argv[2];

// Check if x can be converted to an integer
if (isNaN(x)) {
  // x is not a number
  console.log("Missing number of occurrences");
} else {
  // Print "C is fun" x times
  for (let i = 0; i < x; i++) {
    console.log("C is fun");
  }
}
