(function () {
  var button = document.querySelector("#theme");
  if (!button) return;

  function systemTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function activeTheme() {
    return document.documentElement.dataset.theme || systemTheme();
  }

  function paintTheme(choice) {
    if (choice) document.documentElement.dataset.theme = choice;
    else delete document.documentElement.dataset.theme;
    var next = activeTheme() === "dark" ? "Light" : "Dark";
    button.textContent = next;
    button.setAttribute("aria-label", "Switch to " + next.toLowerCase() + " theme");
  }

  button.addEventListener("click", function () {
    var next = activeTheme() === "dark" ? "light" : "dark";
    localStorage.setItem("theme", next);
    paintTheme(next);
  });

  var saved = localStorage.getItem("theme");
  paintTheme(saved === "light" || saved === "dark" ? saved : "");
})();
