#!/usr/bin/node

exports.esrever = function (list) {
    // Initialize an array
    const reversedList = [];
  
    // Iterate in reverse order
    for (let u = list.length - 1; u >= 0; u--) {
      // Add each element to the reversed list
      reversedList.push(list[u]);
    }
  
    return reversedList;
  };
