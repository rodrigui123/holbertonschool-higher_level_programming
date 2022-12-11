#!/usr/bin/node

const size = process.argv[2];

if (isNaN(size)) {
  // size is not a number
  console.log('Missing size');
} else {
  // size is a number
  // Print a square of size x size
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
