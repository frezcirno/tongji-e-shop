"use strict"

function parseUrl(url) {
    var result = [];
    var query = url.split("?")[1] || '';
    var queryArr = query.split("&");
    queryArr.forEach(function (item) {
        var obj = {};
        var value = item.split("=")[1];
        var key = item.split("=")[0];
        obj[key] = value;
        result.push(obj);
    });
    return result;
}

function login() {
    let email = document.querySelector("#email").value;
    let password = document.querySelector("#password").value;
    let error = document.querySelector("#error");
    error.textContent = "";
    if (email === '') {
        error.textContent = "账号不能为空";
        document.querySelector("#email").classList.add("input-err")
        return;
    }
    document.querySelector("#email").classList.remove("input-err")
    if (password === '') {
        error.textContent = "密码不能为空";
        document.querySelector("#password").classList.add("input-err")
        return;
    }
    document.querySelector("#password").classList.remove("input-err")
    ajax({
        type: "POST",
        url: "/api/login",
        data: {
            email,
            password
        },
        success(res) {
            console.log(res);
            let args = parseUrl(window.location.href);
            if (args.src)
                window.location.href = args.src;
            else
                window.location.href = res.location;
        },
        fail(err) {
            console.log(err);
        }
    })
}