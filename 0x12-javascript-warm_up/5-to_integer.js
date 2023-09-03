#!/usr/bin/nod
e
/* script that prints My number: <first argument converted in integer> */
const arg = process.argv[2];
const num = Math.floor(Number(process.argv[2]));
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
