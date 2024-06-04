const elements = document.querySelectorAll('.element');
elements.forEach((el, index) => {
    setTimeout(() => {
        el.classList.add('show');
    }, index * 250);
});