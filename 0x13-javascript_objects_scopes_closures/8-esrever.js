#!/usr/bin/node
// function that returns the reversed version of a list:
// Define a function that reverses a list without using reverse
exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
