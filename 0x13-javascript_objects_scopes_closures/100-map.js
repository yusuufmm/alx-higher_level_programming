#!/usr/bin/node
//  script that imports an array and computes a new array.
const list = require('./100-data.js').list;
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log(list);
