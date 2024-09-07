#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching film data:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error(`Error: Unable to fetch film data for Movie ID ${movieId}`);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Error: Unable to fetch character data from ${characterUrl}`);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
