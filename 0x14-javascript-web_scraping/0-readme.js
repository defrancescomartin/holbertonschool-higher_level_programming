#!/usr/bin/node
/* Script that reads and prints the content of a file */

const fileName = process.argv[2];
const fs = require('fs');
fs.readFile(fileName, 'utf8', (error, data) => {
  console.log(error || data);
});
