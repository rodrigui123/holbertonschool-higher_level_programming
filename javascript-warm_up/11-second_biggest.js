#!/usr/bin/node

// Get the list of arguments
let numbers = process.argv.slice(2);

// If no arguments were passed, print 0
if (numbers.length === 0) {
  console.log(0);
    return;
}

// If only one argument was passed, print 0
if (numbers.length === 1) {
  console.log(0);
  return;
}

// Convert the arguments to integers
numbers = numbers.map(n => parseInt(n));

// Sort the numbers in ascending order
numbers.sort((a, b) => a - b);

// The second biggest number is the one before the last
let secondBiggest = numbers[numbers.length - 2];

// Print the second biggest number
console.log(secondBiggest);
