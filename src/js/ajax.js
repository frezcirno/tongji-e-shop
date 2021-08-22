
function ajax(options = {}) {
    let { url, type, data, success, fail, contentType, rawdata } = options;
    url = '/tongji-e-shop' + url;
    type = (type || "GET").toUpperCase();
    contentType = contentType || "application/x-www-form-urlencoded"
    let params = rawdata || toParams(data);

    let xhr = new XMLHttpRequest();
    xhr.onreadystatechange = () => {
        if (xhr.readyState === 4) {
            if (xhr.status >= 200 && xhr.status < 300) {
                success && success(JSON.parse(xhr.responseText));
            } else if (xhr.status >= 400) {
                fail && fail(JSON.parse(xhr.responseText));
            }
        }
    };

    if (type === "GET") {
        xhr.open(type, url + (params || '?') + params);
        xhr.send();
    } else {
        xhr.open(type, url);
        xhr.setRequestHeader('Content-Type', contentType);
        xhr.send(params);
    }
}
/**
 * 对象参数的处理
 * @param data
 * @returns {string}
 */
function toParams(data) {
    var arr = [];
    for (var param in data) {
        arr.push(encodeURIComponent(param) + '=' + encodeURIComponent(data[param]));
    }
    // console.log(arr);
    arr.push(('randomNumber=' + Math.random()).replace('.', ''));
    // console.log(arr);
    return arr.join('&');
}
