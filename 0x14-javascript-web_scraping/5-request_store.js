#!/usr/bin/node
/* Script that gets the contents of a webpage and stores it in a file */

const axios = require('axios').default;
axios({
  method: 'get',
  url: process.argv[2]
})
  .then(function (response) {
    const fileName = process.argv[3];
    const text = response.data;
    const fs = require('fs');
    fs.writeFile(fileName, text, (error) => {
      error && console.log(error);
    });
  });
