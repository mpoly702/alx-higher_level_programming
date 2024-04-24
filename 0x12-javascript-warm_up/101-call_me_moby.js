#!/usr/bin/node

// Define module that exports an obj
module.exports = {
  // The method callMeMoby takes two param
  callMeMoby: function (v, theFunction) {
    // Loop v times
    for (let u = 0; u < v; u++) {
      // Execute the given function
      theFunction();
    }
  }
};
