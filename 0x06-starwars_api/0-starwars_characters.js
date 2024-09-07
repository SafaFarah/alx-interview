#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;
request(movieUrl, (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const characterUrls = JSON.parse(body).characters;
      fetchCharacter(characterUrls, 0);
    }
  }
);
const fetchCharacter = (urls, index) => {
  if (index === urls.length) return;
  request(urls[index], (error, response, body) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(body).name);
      fetchCharacter(urls, index + 1);
    }
  });
};
