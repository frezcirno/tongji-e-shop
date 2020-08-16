'use strict'

var current_swipe = 0;

setInterval(swipeNext, 3000);

function swipeTo(i) {
    current_swipe = i % 5;
    let last = (current_swipe - 1) % 5;

    let slides = document.querySelectorAll('.swiper-slide');
    slides.forEach((slide, i) => {
        if (i == last)
            slide.style = "transform: translateX(-1226px);";
        else
            slide.style = "transform: translateX(" + 1226 * ((i - current_swipe + 5) % 5) + "px);";
    })

    let bullets = document.querySelectorAll('.swiper-pagination-bullet');
    bullets.forEach(bullet => {
        bullet.classList.remove('swiper-pagination-bullet-active')
    });
    bullets[current_swipe].classList.add('swiper-pagination-bullet-active');
}

function swipePrev() {
    swipeTo(current_swipe - 1);
}

function swipeNext() {
    swipeTo(current_swipe + 1);
}

