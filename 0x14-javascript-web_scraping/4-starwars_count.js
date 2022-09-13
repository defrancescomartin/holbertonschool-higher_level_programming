#!/usr/bin/node
/* Script prints the title of a Star Wars movie where the
    episode number matches a given integer.
*/

const axios = require('axios').default;
const starWars = 'https://swapi-api.hbtn.io/api/people/18/';
axios.get(process.argv[2])
  .then(function (response) {
    let num = 0;
    for (const x in response.data.results) {
      if (response.data.results[x].characters.includes(starWars)) {
        num = num + 1;
      }
    }
    console.log(num);
  })
  .catch(function (error) {
    error = '0';
    console.log(error);
  });
