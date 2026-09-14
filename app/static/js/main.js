// ---------------------------------------------------------
// Main JavaScript for the PhD student website.
// Handles: mobile navigation toggle, publication filtering,
// and smooth scrolling for on-page anchor links.
// ---------------------------------------------------------

document.addEventListener("DOMContentLoaded", function () {

    // --- Mobile navigation toggle ---
    var navToggle = document.getElementById("navToggle");
    var primaryNav = document.getElementById("primaryNav");

    if (navToggle && primaryNav) {
        navToggle.addEventListener("click", function () {
            var isOpen = primaryNav.classList.toggle("open");
            navToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
        });

        // Close the mobile menu after a link is clicked.
        primaryNav.querySelectorAll("a").forEach(function (link) {
            link.addEventListener("click", function () {
                primaryNav.classList.remove("open");
                navToggle.setAttribute("aria-expanded", "false");
            });
        });
    }

    // --- Publication filtering (by type) ---
    var filterButtons = document.querySelectorAll("#pubFilter .filter-btn");
    var publicationItems = document.querySelectorAll(".publication-item");

    filterButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            filterButtons.forEach(function (b) { b.classList.remove("active"); });
            button.classList.add("active");

            var filter = button.getAttribute("data-filter");

            publicationItems.forEach(function (item) {
                if (filter === "all" || item.getAttribute("data-type") === filter) {
                    item.style.display = "";
                } else {
                    item.style.display = "none";
                }
            });
        });
    });

    // --- Smooth scrolling for in-page anchors ---
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
        anchor.addEventListener("click", function (e) {
            var targetId = this.getAttribute("href").slice(1);
            var target = document.getElementById(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
