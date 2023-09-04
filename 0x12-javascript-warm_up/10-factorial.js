#!/usr/bin/node
function factorial (n) {
  // Base case: Factorial of NaN is 1
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(Number(process.argv[2])));
