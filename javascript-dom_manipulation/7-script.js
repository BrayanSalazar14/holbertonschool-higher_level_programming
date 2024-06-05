document.addEventListener('DOMContentLoaded', (event) => {
  const listMovies = document.querySelector('#list_movies');
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(results => results.json())
    .then(data => {
      for (const result of data.results) {
        const movie = document.createElement('Li');
        movie.textContent = result.title;
        listMovies.appendChild(movie);
      }
    });
});
