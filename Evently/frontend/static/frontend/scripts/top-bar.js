window.addEventListener("scroll", function () {
  const topBar = document.querySelector(".top-bar");
  if (window.scrollY < window.innerHeight) {
    topBar.style.backgroundColor = `rgba(0,0,0,0.0)`;
  } else {
    topBar.style.backgroundColor = 'rgba(0,0,0,1)';
  }
});