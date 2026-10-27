document.addEventListener("DOMContentLoaded", () => {
  const iconNode = document.querySelector(".navbar i.bi-moon, .navbar i.bi-sun");
  const toggleLink =
    (iconNode && iconNode.closest("a")) ||
    document.querySelector('.navbar a[href="#theme-toggle"]');
  if (!toggleLink) {
    return;
  }

  // The class lives on <html>; theme-init.html sets it before first paint.
  const root = document.documentElement;
  const icon = toggleLink.querySelector("i");

  const applyTheme = (isDark) => {
    root.classList.toggle("theme-dark", isDark);
    if (icon) {
      icon.classList.toggle("bi-moon", !isDark);
      icon.classList.toggle("bi-sun", isDark);
    }
  };

  applyTheme(root.classList.contains("theme-dark"));

  toggleLink.setAttribute("role", "button");
  toggleLink.setAttribute("aria-label", "Toggle dark mode");

  toggleLink.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    const nextDark = !root.classList.contains("theme-dark");
    applyTheme(nextDark);
    try {
      localStorage.setItem("theme", nextDark ? "dark" : "light");
    } catch (e) {}

    const collapse = document.querySelector(".navbar .navbar-collapse.show");
    if (collapse && window.bootstrap?.Collapse) {
      const instance =
        window.bootstrap.Collapse.getInstance(collapse) ||
        new window.bootstrap.Collapse(collapse, { toggle: false });
      instance.hide();
    }
  });
});
