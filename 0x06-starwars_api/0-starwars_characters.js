#!/usr/bin/node

const request = require('request');

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

request(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const characterUrls = JSON.parse(body).characters;
      fetchCharacter(characterUrls, 0);
    }
  }
);
