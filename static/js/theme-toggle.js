document.addEventListener("DOMContentLoaded", () => {
    const themeToggle = document.getElementById("theme-toggle");
    const themeIcon = document.getElementById("theme-icon");
    const bootstrapLink = document.getElementById("bootstrap-theme");
    const navbar = document.querySelector("nav.navbar");

    const lightTheme = themeToggle.dataset.light;
    const darkTheme = themeToggle.dataset.dark;

    const applyTheme = (theme) => {
        if (theme === "dark") {
            bootstrapLink.href = darkTheme;
            themeIcon.classList.remove("bi-sun-fill");
            themeIcon.classList.add("bi-moon-fill");

            navbar.classList.remove("bg-light");
            navbar.classList.add("bg-dark");
            navbar.setAttribute("data-bs-theme", "dark");
        } else {
            bootstrapLink.href = lightTheme;
            themeIcon.classList.remove("bi-moon-fill");
            themeIcon.classList.add("bi-sun-fill");

            navbar.classList.remove("bg-dark");
            navbar.classList.add("bg-light");
            navbar.setAttribute("data-bs-theme", "light");
        }
    };

    const savedTheme = localStorage.getItem("theme") || "light";
    applyTheme(savedTheme); // Aplicar tema al cargar

    themeToggle.addEventListener("click", (e) => {
        e.preventDefault();
        const currentTheme = localStorage.getItem("theme") || "light";
        const newTheme = currentTheme === "light" ? "dark" : "light";
        localStorage.setItem("theme", newTheme);
        applyTheme(newTheme);
    });
});
