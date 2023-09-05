#!/usr/bin/node
//  script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data.js').dict;
// Create a new dictionary to store user ids by occurrence
const usersByOccurrence = {};
for (const userId in dict) {
  const occurrence = dict[userId];

  // If the occurrence is not a key in the new dictionary, create it
  if (!(occurrence in usersByOccurrence)) {
    usersByOccurrence[occurrence] = [];
  }
  usersByOccurrence[occurrence].push(userId);
}
console.log(usersByOccurrence);
