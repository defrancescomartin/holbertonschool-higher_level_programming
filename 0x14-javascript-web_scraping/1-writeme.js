#!/usr/bin/node
/* Script that writes a string to a file
    The first argument is the file path
    The second argument is the string to write
    The content of the file must be written in utf-8
    If an error occurred during while writing, print the error object
*/

const fileName = process.argv[2];
const text = process.argv[3];
const fs = require('fs');
fs.writeFile(fileName, text, (error) => {
  error && console.log(error);
});
