#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.writeFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
});
