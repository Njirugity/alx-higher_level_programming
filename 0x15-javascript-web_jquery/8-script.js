$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format', function (data) {
    const title = data.results;
    title.forEach(function (movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
