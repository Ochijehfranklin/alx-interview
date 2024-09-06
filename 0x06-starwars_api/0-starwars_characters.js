#!/usr/bin/env node
/**
 * Prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const request = require('request');
const filmId = process.argv[2] + '/';
const filmUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(filmUrl + filmId, async (err, res, body) => {
  if (err) return console.error(err);

  // find URLs of each character in the film as a list obj
  const charURLList = JSON.parse(body).characters;

  // Use URL list to character pages to make new requests
  // await queues requests until they resolve in order
  for (const charURL of charURLList) {
    await new Promise((resolve, reject) => {
      request(charURL, (err, res, body) => {
        if (err) return console.error(err);

        // finds each character name and prints in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
