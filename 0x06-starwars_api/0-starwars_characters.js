#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(movieUrl, (error, response, body) => {
  if (error) {
    return;
  }
  let movieData;
  try {
    movieData = JSON.parse(body);
  } catch (err) {
    return;
  }
  const characterUrls = movieData.characters;
  const fetchCharacters = async () => {
    for (const characterUrl of characterUrls) {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request(characterUrl, (err, res, characterBody) => {
            if (err) {
              reject(err);
            } else {
              resolve(characterBody);
            }
          });
        });
        const characterData = JSON.parse(characterResponse);
        console.log(characterData.name);
      } catch (err) {
        console.error('Error fetching or parsing character data:', err);
      }
    }
  };
  fetchCharacters().catch(err => {
    return;
  });
});
