#!/usr/bin/node

const axios = require('axios');

const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

axios.get(url)
  .then(response => {
    const characters = response.data.characters;
    characters.forEach(characterUrl => {
      axios.get(characterUrl)
        .then(characterResponse => {
          console.log(characterResponse.data.name);
        })
        .catch(error => {
          console.log(`Error fetching character: ${error.message}`);
        });
    });
  })
  .catch(error => {
    console.log(`Error fetching movie: ${error.message}`);
  });
