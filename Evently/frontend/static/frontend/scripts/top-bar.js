window.addEventListener("scroll", function () {
  const topBar = document.querySelector(".top-bar");
  if (window.scrollY < window.innerHeight) {
    topBar.style.backgroundColor = "transparent";
  } else {
    topBar.style.backgroundColor = "rgba(178, 171, 46, 1)";
  }
});