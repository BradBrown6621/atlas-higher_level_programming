#!/usr/bin/node

$(function () {
  const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(url, function (data) {
    for (item of data.results) {
      $('ul#list_movies').append(`<li>${item.title}</li>`);
    }
  });
});
