#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle of 4-rectangle.js
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
