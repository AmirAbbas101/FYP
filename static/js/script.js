// Get DOM Elements
const toggleMenuOpenButton = document.getElementById("toggleOpen");
const toggleMenuCloseButton = document.getElementById("toggleClose");
const collapsibleMenu = document.getElementById("collapseMenu");

const profileAvatarButton = document.getElementById("avatarButton");
const userDropdownMenu = document.getElementById("userDropdown");

const passwordField = document.getElementById("password");
const confirmPasswordField = document.getElementById("confirmPassword");

// Ensure element exists before applying actions
function isElementExists(element) {
  return element !== null && typeof element !== "undefined";
}

// Toggle Element Visibility
function toggleVisibility(element) {
  const computedStyle = window.getComputedStyle(element);
  const isVisible = computedStyle.display === "block";
  element.style.display = isVisible ? "none" : "block";
}

// Toggle Menu Visibility Event
function setupMenuToggleButtons() {
  if (
    isElementExists(toggleMenuOpenButton) &&
    isElementExists(toggleMenuCloseButton)
  ) {
    toggleMenuOpenButton.addEventListener("click", () =>
      toggleVisibility(collapsibleMenu)
    );
    toggleMenuCloseButton.addEventListener("click", () =>
      toggleVisibility(collapsibleMenu)
    );
  }
}

// Toggle User Dropdown Event
function setupProfileDropdownToggle() {
  if (isElementExists(profileAvatarButton)) {
    profileAvatarButton.addEventListener("click", () => {
      userDropdownMenu.classList.toggle("hidden");
    });
  }
}

// Validate Passwords
function arePasswordsMatching(password, confirmPassword) {
  return password === confirmPassword;
}

// Password Validation Event
function setupPasswordValidation() {
  const form = document.querySelector("form");
  if (
    isElementExists(form) &&
    isElementExists(passwordField) &&
    isElementExists(confirmPasswordField)
  ) {
    form.addEventListener("submit", function (event) {
      const password = passwordField.value.trim();
      const confirmPassword = confirmPasswordField.value.trim();

      if (!arePasswordsMatching(password, confirmPassword)) {
        alert("Passwords do not match!");
        event.preventDefault(); // Prevent form submission
      }
    });
  }
}

// Initialize Event Listeners
function initializeEventListeners() {
  setupMenuToggleButtons();
  setupProfileDropdownToggle();
  setupPasswordValidation();
}

// Run Event Listeners Setup on DOM Content Loaded
document.addEventListener("DOMContentLoaded", () => {
  initializeEventListeners();
});

// Browse-jobs.html
$(document).ready(function () {
  $(".jobs-filter").click(function () {
    // Toggle the dropdown just below the clicked header
    $(this).next(".jobs-filter-dropdown").toggleClass("hidden flex");
    // Toggle the arrow icon in the clicked header
    $(this)
      .find(".arrow")
      .toggleClass("ri-arrow-up-s-line ri-arrow-down-s-line");
  });
});
