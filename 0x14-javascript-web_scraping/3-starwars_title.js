#!/usr/bin/node
/* Script prints the title of a Star Wars movie where the
    episode number matches a given integer.
*/

const axios = require('axios').default;
const starWars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
axios.get(starWars)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(error);
  });
