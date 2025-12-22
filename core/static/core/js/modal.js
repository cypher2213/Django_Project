document.addEventListener('DOMContentLoaded', () => {
    const menu = document.getElementById('menu');
    const openBtn = document.getElementById('burgerBtn');
    const closeBtn = document.getElementById('closeMenu');

    openBtn.addEventListener('click', () => menu.classList.add('is-open'));
    closeBtn.addEventListener('click', () => menu.classList.remove('is-open'));
    window.addEventListener('click', (e) => {
        if (e.target === menu) menu.classList.remove('is-open');
    });
});
