#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

// Iterate over the keys (user ids) and values occurrence
Object.keys(dict).forEach(user => {
  const occurrence = dict[user];

  // If not a key, create a new key with an array containing userID
  if (!newDict[occurrence]) {
    newDict[occurrence] = [user];
  } else {
    // If already a key, push the user id to its array
    newDict[occurrence].push(user);
  }
});

console.log(newDict);
