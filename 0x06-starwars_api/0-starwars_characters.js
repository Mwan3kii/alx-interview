#!/usr/bin/node

const request = require('request-promise-native');

async function fetchCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const filmData = await request({ uri: url, json: true });
    const charactersUrls = filmData.characters;

    const characterPromises = charactersUrls.map(url => request({ uri: url, json: true }));
    const charactersData = await Promise.all(characterPromises);

    charactersData.forEach(character => {
      console.log(character.name);
    });
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

fetchCharacters(movieId);
