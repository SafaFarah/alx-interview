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
  characterUrls.forEach((characterUrl) => {
    request(characterUrl, (err, res, characterBody) => {
      if (err) {
        return;
      }
      let characterData;
      try {
        characterData = JSON.parse(characterBody);
      } catch (err) {
        return;
      }
      console.log(characterData.name);
    });
  });
});
