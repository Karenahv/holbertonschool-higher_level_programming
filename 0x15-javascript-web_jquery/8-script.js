$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi.co/api/films/?format=json',
    success: function (movies) {
      $.each(movies, function (i, movie) {
        $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
      });
    }
  });
});
