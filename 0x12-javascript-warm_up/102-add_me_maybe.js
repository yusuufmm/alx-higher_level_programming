#!/usr/bin/node
exports.addMeMaybe = function incrementAndCall (number, theFunction) {
  theFunction(number + 1);
};
