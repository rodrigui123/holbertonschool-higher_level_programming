#!/usr/bin/node
const Squaree = require('./5-square');

module.exports = class Square extends Squaree {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
