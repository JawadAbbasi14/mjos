(function () {
    "use strict";

    var root = document.documentElement;
    var initialTheme = root.getAttribute("data-theme") === "dark" ? "dark" : "light";

    document.addEventListener("DOMContentLoaded", function () {
        var toggle = document.getElementById("theme-toggle");
        var icon = toggle && toggle.querySelector(".theme-toggle__icon");
        var label = toggle && toggle.querySelector(".theme-toggle__label");
        var themeColor = document.querySelector('meta[name="theme-color"]');

        function syncTheme(theme) {
            var isDark = theme === "dark";
            root.setAttribute("data-theme", theme);
            if (toggle) {
                toggle.setAttribute("aria-pressed", String(isDark));
                toggle.setAttribute("aria-label", isDark ? "Switch to light theme" : "Switch to dark theme");
            }
            if (icon) {
                icon.textContent = isDark ? "\u2600" : "\u263e";
            }
            if (label) {
                label.textContent = isDark ? "Day" : "Night";
            }
            if (themeColor) {
                themeColor.setAttribute("content", isDark ? "#0d1210" : "#f3ead9");
            }
        }

        syncTheme(initialTheme);

        if (toggle) {
            toggle.addEventListener("click", function () {
                var nextTheme = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
                syncTheme(nextTheme);
                try {
                    window.localStorage.setItem("mjos-theme", nextTheme);
                } catch (error) {
                    // The current page still changes theme when storage is unavailable.
                }
            });
        }
    });
})();