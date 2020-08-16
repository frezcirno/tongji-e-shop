'use strict'

function onsearch(e) {
    e.preventDefault();
    let text = document.querySelector('.form-text').value;
    console.log(text);
}

function logout() {
    ajax({
        type: "POST",
        url: "/api/logout",
        success(res) {
            window.location.href = "/"
        },
        fail(err) {

        }
    })
}