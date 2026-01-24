document.addEventListener("DOMContentLoaded", () => {
  const iconNode = document.querySelector(".navbar i.bi-moon, .navbar i.bi-sun");
  const toggleLink =
    (iconNode && iconNode.closest("a")) ||
    document.querySelector('.navbar a[href="#theme-toggle"]');
  if (!toggleLink) {
    return;
  }

  const body = document.body;
  const icon = toggleLink.querySelector("i");

  const applyTheme = (isDark) => {
    body.classList.toggle("theme-dark", isDark);
    if (icon) {
      icon.classList.toggle("bi-moon", !isDark);
      icon.classList.toggle("bi-sun", isDark);
    }
  };

  const stored = localStorage.getItem("theme");
  if (stored) {
    applyTheme(stored === "dark");
  }

  toggleLink.setAttribute("role", "button");
  toggleLink.setAttribute("aria-label", "Toggle dark mode");

  toggleLink.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    const nextDark = !body.classList.contains("theme-dark");
    applyTheme(nextDark);
    localStorage.setItem("theme", nextDark ? "dark" : "light");

    const collapse = document.querySelector(".navbar .navbar-collapse.show");
    if (collapse && window.bootstrap?.Collapse) {
      const instance =
        window.bootstrap.Collapse.getInstance(collapse) ||
        new window.bootstrap.Collapse(collapse, { toggle: false });
      instance.hide();
    }
  });
});
