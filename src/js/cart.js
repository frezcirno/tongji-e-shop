"use strict"

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".cart-item").forEach(item => {
        calc(item);
    })
    selall(true);
})

function selall(checked) {
    let checks = document.querySelectorAll(".col-check input");
    checks.forEach(check => {
        check.checked = checked;
    })
}

function order() {
    let items = document.querySelectorAll(".cart-item")
    items = Array.prototype.filter.call(items, function (node) {
        return node.querySelector('.check-box').checked;
    })
    items = Array.prototype.map.call(items, function (node) {
        return {
            id: Number(node.attributes["item-id"].value),
            count: Number(node.querySelector('.num').value)
        }
    })
    ajax({
        type: "POST",
        url: "/api/addorder",
        contentType: 'application/json',
        rawdata: JSON.stringify({ items }),
        success(res) {
            window.location.href = res.location;
        },
        fail(err) {
            console.log(err);
        }
    })
}

function del(e) {
    e = e.target.parentNode.parentNode;

    var itemid = Number(e.attributes["item-id"].value)

    ajax({
        type: "POST",
        url: "/api/delcart",
        data: { itemid },
        success(res) {
            e.remove();
            resum();
            recount();
            recheck();
        },
        fail(err) {
        }
    })

}

function minus(e) {
    e = e.target;
    let v = e.parentNode.children[1]
    if (v.value <= 1) return
    v.value--;
    calc(e.parentNode.parentNode.parentNode);
}

function plus(e) {
    e = e.target;
    e.parentNode.children[1].value++;
    calc(e.parentNode.parentNode.parentNode);
    resum();
}

function calc(item) {
    let count = item.querySelector(".col-price span").textContent;
    let val = item.querySelector(".col-num .num").value;
    let total = item.querySelector(".col-total span");
    total.textContent = val * count;
    resum();
}

function resum() {
    let totals = document.querySelectorAll(".cart-item");
    let resum = 0;
    totals = [...totals].filter(total =>
        total.querySelector(".col-check input").checked && total
    );
    totals.forEach(total => {
        total = total.querySelector(".col-total span").textContent;
        resum += Number(total);
    })
    document.querySelector(".total-price em").textContent = resum;
}

function recount() {
    let items = document.querySelectorAll(".cart-item")
    document.querySelectorAll(".cart-total span")[0].textContent = items.length;
}

function recheck() {
    let checks = document.querySelectorAll(".cart-item .col-check .check-box")
    checks = [...checks].filter(check => check.checked && check);
    document.querySelectorAll(".cart-total span")[1].textContent = checks.length;
    resum();
}

document.addEventListener('DOMContentLoaded', () => {
    document.querySelector(".list-head .col-check input").click();
    recount();
    recheck();
    // resum();
})

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