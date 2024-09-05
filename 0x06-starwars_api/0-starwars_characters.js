#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function sendRequest (characterList, index) {
  if (characterList.length === index) {
    return;
  }

  axios(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      sendRequest(characterList, index + 1);
    }
  });
}

axios(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characterList = JSON.parse(body).characters;

    sendRequest(characterList, 0);
  }
});
