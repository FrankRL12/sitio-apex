const burger = document.querySelector('.burger');
const links = document.querySelector('.links');

burger.addEventListener('click', () => {
  burger.classList.toggle('active');
  links.classList.toggle('active');
});
