
let count = 0;
function changeImage(src) {
    document.querySelector("img").src = "../images/" + src + ".png";
}

document.body.onmousedown = function () {
    count += 1;
    document.querySelector("#pop").textContent = count;
    changeImage("下載 (1)");
}
document.body.onmouseup= function () {
    changeImage("下載");
}
  
