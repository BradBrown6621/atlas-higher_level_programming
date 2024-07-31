#!/usr/bin/node

$(function () {
  $('div#red_header').on('click', function () {
    $('header').css('color', 'red');
  });
});
