// Trigger the Read the Docs Addons Search modal when focusing the search input
// NOTE: Adjust the selector if your theme changes the search box markup
document.addEventListener("DOMContentLoaded", function () {
  var input = document.querySelector("[role='search'] input");
  if (!input) return;
  input.addEventListener("focusin", function () {
    var event = new CustomEvent("readthedocs-search-show");
    document.dispatchEvent(event);
  });
});


