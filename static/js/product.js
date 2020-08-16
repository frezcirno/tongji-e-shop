"use strict"

// var total_swipe = 3
// var current_swipe = 0;

// document.addEventListener("DOMContentLoaded", function () {
//     total_swipe = document.querySelectorAll(".img-slide").length;
//     setInterval(swipeNext, 3000);
// })

// function swipeTo(i) {
//     current_swipe = i % total_swipe;
//     let last = (current_swipe - 1) % total_swipe;

//     let slides = document.querySelectorAll('.swiper-slide');
//     slides.forEach((slide, i) => {
//         if (i == last)
//             slide.style = "transform: translateX(-1226px);";
//         else
//             slide.style = "transform: translateX(" + 1226 * ((i - current_swipe + total_swipe) % total_swipe) + "px);";
//     })

//     let bullets = document.querySelectorAll('.swiper-pagination-bullet');
//     bullets.forEach(bullet => {
//         bullet.classList.remove('swiper-pagination-bullet-active')
//     });
//     bullets[current_swipe].classList.add('swiper-pagination-bullet-active');
// }

// function swipePrev() {
//     swipeTo(current_swipe - 1);
// }

// function swipeNext() {
//     swipeTo(current_swipe + 1);
// }


function buy() {
    ajax({
        type: "POST",
        url: "/api/buy",
        data: {
            itemid: window.location.href.split('/').pop(),
            count: 1
        },
        success(res) {
            console.log("成功");
        },
        fail(err) {
            console.log("失败")
        }
    })
}

function addcart() {
    ajax({
        type: "POST",
        url: "/api/addcart",
        data: {
            itemid: window.location.href.split('/').pop(),
            count: 1
        },
        success(res) {
            window.location.reload();
        },
        fail(err) {
            window.location.href = err.location;
        }
    })
}

function updatecart() {
    ajax({
        type: "GET",
        url: "/api/cart",
        success(res) {
            document.querySelector(".cart-num").textContent = res.data.length;
        }
    })
}