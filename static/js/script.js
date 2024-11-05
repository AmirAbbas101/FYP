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

// Login and Sign up form validation
// Validate Passwords
function arePasswordsMatching(password, confirmPassword) {
  return password === confirmPassword;
}

function arePasswordVaild(password) {
  const isValidPassword = /^(?=.*?[0-9])(?=.*?[A-Za-z]).{8,32}$/;
  return isValidPassword.test(password);
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

  $("#btn-filter").click(function () {
    $("aside").toggleClass("hidden block");
  });
  $("#btn-apply-filter").click(function () {
    $("aside").toggleClass("hidden block");
  });
});

// Settings.html
$(document).ready(function () {
  $("#btn-sidebar-toggle").on("click", () => {
    $("#sidebar").toggleClass("hidden");
    $("#btn-sidebar-toggle").toggleClass("ri-menu-fill ri-close-large-line");
  });
});

$(document).ready(function () {
  const $profileTab = $("#my-profile-settings");
  const $loginDetailsTab = $("#login-details-settings");
  const $notificationTab = $("#notifications-settings");
  const $btnProfileTab = $("#btn-my-profile");
  const $btnLoginDetailsTab = $("#btn-login-details");
  const $btnNotificationTab = $("#btn-notifications");

  const hiddenClass = "hidden";
  const activeClass = "active";

  function toggleActiveTab(showTab, ...hideTabs) {
    showTab.removeClass(hiddenClass);
    hideTabs.forEach((tab) => tab.addClass(hiddenClass));
  }

  function setActiveButton(activeButton, ...inactiveButtons) {
    activeButton.addClass(activeClass);
    inactiveButtons.forEach((button) => button.removeClass(activeClass));
  }

  $btnProfileTab.on("click", () => {
    toggleActiveTab($profileTab, $loginDetailsTab, $notificationTab);
    setActiveButton($btnProfileTab, $btnLoginDetailsTab, $btnNotificationTab);
  });

  $btnLoginDetailsTab.on("click", () => {
    toggleActiveTab($loginDetailsTab, $profileTab, $notificationTab);
    setActiveButton($btnLoginDetailsTab, $btnProfileTab, $btnNotificationTab);
  });

  $btnNotificationTab.on("click", () => {
    toggleActiveTab($notificationTab, $profileTab, $loginDetailsTab);
    setActiveButton($btnNotificationTab, $btnProfileTab, $btnLoginDetailsTab);
  });
});
