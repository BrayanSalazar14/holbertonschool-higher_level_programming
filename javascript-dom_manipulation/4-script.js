document.addEventListener('DOMContentLoaded', (event) => {
  const item = document.querySelector('#add_item');
  item.addEventListener('click', () => {
    const unorderedList = document.querySelector('.my_list');
    const list = document.createElement('LI');
    list.textContent = 'Item';
    unorderedList.appendChild(list);
  });
});
