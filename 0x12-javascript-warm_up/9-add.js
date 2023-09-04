#!/usr/bin/node
/* script that prints the addition of 2 */
function add (a, b) {
  return a + b;
}
const arg1 = parseInt(process.argv[2]);

const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  console.log(add(arg1, arg2));
} else {
  console.log('Please provide two valid integers.');
}
