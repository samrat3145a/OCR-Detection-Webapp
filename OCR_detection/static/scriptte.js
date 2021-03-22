const loginPopup = document.querySelector(".login-popup");
const close = document.querySelector(".close");

window.addEventListener("load", function () {
  showPopup();
});

function showPopup() {
  loginPopup.classList.add("show");
}

close.addEventListener("click", function () {
  loginPopup.classList.remove("show");
});
