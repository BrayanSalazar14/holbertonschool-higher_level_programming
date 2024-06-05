document.addEventListener('DOMContentLoaded', (event) => {
  const toogleHeader = document.querySelector('#toggle_header');
  toogleHeader.addEventListener('click', () => {
    const header = document.querySelector('header');
    if (header.classList.value === 'green') header.classList.value = 'red';
    else header.classList.value = 'green';
  });
});
