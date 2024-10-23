// script.js

window.addEventListener('load', function() {
  // Get all images with the 'thumbnail' class
  const thumbnails = document.querySelectorAll('img.thumbnail');

  thumbnails.forEach((img) => {
    const highResUrl = img.getAttribute('data-fullres');
    loadHighResImage(img, highResUrl);
  });
});

function loadHighResImage(elem, highResUrl) {
  let image = new Image();
  image.addEventListener('load', () => elem.src = highResUrl); // Swap to high-res when it's fully loaded
  image.src = highResUrl;
}

function toggleScale(element) {
    element.classList.toggle("scaled");
  }