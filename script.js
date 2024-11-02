function toggleScale(element) {
    if (element.naturalWidth > element.naturalHeight) {
        element.classList.toggle("horizontal");
    } else {
        element.classList.toggle("vertical");
    }
}