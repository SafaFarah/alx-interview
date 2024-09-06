#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error) return console.error('Error:', error);
  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  characters.forEach((characterUrl) => {
    request(characterUrl, (err, res, body) => {
      if (err) return console.error('Error:', err);
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
