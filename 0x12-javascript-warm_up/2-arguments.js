#!/usr/bin/node
const ar = process.argv.length;

if (ar > 2) {
  console.log('Argument' + (ar > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
