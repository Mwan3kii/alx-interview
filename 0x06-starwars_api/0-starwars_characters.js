#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];

if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Construct the URL to fetch movie details
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to get the movie details
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    // Fetch each character's details and print the name
    characters.forEach(characterUrl => {
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
          return;
        }

        if (charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } else {
    console.log(`Error: Unable to fetch movie with ID ${movieId}`);
  }
});
