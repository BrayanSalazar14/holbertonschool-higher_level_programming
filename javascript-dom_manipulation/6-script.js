document.addEventListener('DOMContentLoaded', (event) => {
  const character = document.querySelector('#character');
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(resultado => resultado.json())
    .then(datos => {
      character.textContent = datos.name;
    });
});
