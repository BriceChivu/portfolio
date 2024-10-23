// script.js

window.addEventListener('load', function() {
  // Load high-res images once low-res versions are shown
  loadHighResImage(document.getElementById('img1'), 'assets/photos/000012870016.jpg');
  loadHighResImage(document.getElementById('img2'), 'assets/photos/000012870014.jpg');
  loadHighResImage(document.getElementById('img3'), 'assets/photos/000012870038.jpg');
  loadHighResImage(document.getElementById('img4'), 'assets/photos/000012870004.jpg');
});

function loadHighResImage(elem, highResUrl) {
  let image = new Image();
  image.addEventListener('load', () => elem.src = highResUrl); // Swap to high-res when it's fully loaded
  image.src = highResUrl;
}

function toggleScale(element) {
    element.classList.toggle("scaled");
  }