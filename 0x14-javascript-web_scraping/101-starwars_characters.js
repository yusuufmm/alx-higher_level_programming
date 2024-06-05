#!/usr/bin/node
// Completed tasks

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching film:', error);
    return;
  }

  try {
    const content = JSON.parse(body);
    const characters = content.characters;

    characters.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching character:', error);
          return;
        }

        try {
          const character = JSON.parse(body);
          console.log(character.name);
        } catch (parseError) {
          console.error('Error parsing character JSON:', parseError);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing film JSON:', parseError);
  }
});
