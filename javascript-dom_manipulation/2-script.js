document.addEventListener('DOMContentLoaded', (event) => {
  const textHeader = document.querySelector('#red_header');
  textHeader.addEventListener('click', () => {
    const header = document.querySelector('header');
    header.classList.add('red');
  });
});
