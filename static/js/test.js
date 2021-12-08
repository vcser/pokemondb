const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
ctx.fillStyle = 'grey';
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.fillStyle = 'black';
ctx.font = '32px sans-serif';
ctx.fillText("hola mundo", 200, 300);
let counter = 0;
get_static();
function func() {
    alert("hola");
}
function foo() {
    counter += 1;
    document.getElementById("counter").innerHTML = counter;
    update_static();
}
function get_static() {
    fetch(window.origin + "/_num", { method: "GET" }).then(
        function (response) {
            response.text().then(function (text) {
                document.getElementById("static").innerHTML = text
            })
        }
    );
}
function update_static() {
    fetch(window.origin + "/_num", { method: "POST" }).then(
        function (response) {
            response.text().then(function (text) {
                document.getElementById("static").innerHTML = text
            })
        }
    );
}
