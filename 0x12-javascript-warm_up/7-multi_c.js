#!/usr/bin/node
const x = parseInt(process.argv[2]);
let output;
if (isNaN(x)) {
  output = 'Missing number of occurrences';
  console.log(output);
} else {
  output = 'C is fun';
  let i;
  for (i = 0; i < x; i++) {
    console.log(output);
  }
}
