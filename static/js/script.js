// // Get DOM Elements
// const toggleMenuOpenButton = document.getElementById("toggleOpen");
// const toggleMenuCloseButton = document.getElementById("toggleClose");
// const collapsibleMenu = document.getElementById("collapseMenu");

// const profileAvatarButton = document.getElementById("avatarButton");
// const userDropdownMenu = document.getElementById("userDropdown");

// const passwordField = document.getElementById("password");
// const confirmPasswordField = document.getElementById("confirmPassword");

// // Ensure element exists before applying actions
// function isElementExists(element) {
//   return element !== null && typeof element !== "undefined";
// }

// // Toggle Element Visibility
// function toggleVisibility(element) {
//   const computedStyle = window.getComputedStyle(element);
//   const isVisible = computedStyle.display === "block";
//   element.style.display = isVisible ? "none" : "block";
// }

// // Toggle Menu Visibility Event
// function setupMenuToggleButtons() {
//   if (
//     isElementExists(toggleMenuOpenButton) &&
//     isElementExists(toggleMenuCloseButton)
//   ) {
//     toggleMenuOpenButton.addEventListener("click", () =>
//       toggleVisibility(collapsibleMenu)
//     );
//     toggleMenuCloseButton.addEventListener("click", () =>
//       toggleVisibility(collapsibleMenu)
//     );
//   }
// }

// // Toggle User Dropdown Event
// function setupProfileDropdownToggle() {
//   if (isElementExists(profileAvatarButton)) {
//     profileAvatarButton.addEventListener("click", () => {
//       userDropdownMenu.classList.toggle("hidden");
//     });
//   }
// }

// // Login and Sign up form validation
// // Validate Passwords
// function arePasswordsMatching(password, confirmPassword) {
//   return password === confirmPassword;
// }

// // function arePasswordValid(password) {
// //   const isValidPassword = /^(?=.*?[0-9])(?=.*?[A-Za-z]).{8,32}$/;
// //   return isValidPassword.test(password);
// // }

// // Password Validation Event
// function setupPasswordValidation() {
//   const form = document.querySelector("form");
//   if (
//     isElementExists(form) &&
//     isElementExists(passwordField) &&
//     isElementExists(confirmPasswordField)
//   ) {
//     form.addEventListener("submit", function (event) {
//       const password = passwordField.value.trim();
//       const confirmPassword = confirmPasswordField.value.trim();
//       // if (!arePasswordValid(password)) {
//       //   alert("Passwords must contain 1-9 A-Z and a-z!");
//       //   event.preventDefault(); // Prevent form submission
//       // }
//       if (!arePasswordsMatching(password, confirmPassword)) {
//         alert("Passwords do not match!");
//         event.preventDefault(); // Prevent form submission
//       }
//     });
//   }
// }

// // Initialize Event Listeners
// function initializeEventListeners() {
//   setupMenuToggleButtons();
//   setupProfileDropdownToggle();
//   setupPasswordValidation();
// }

// // Run Event Listeners Setup on DOM Content Loaded
// document.addEventListener("DOMContentLoaded", () => {
//   initializeEventListeners();
// });

// $(document).ready(function () {
//   // Browse-jobs.html
//   $(".jobs-filter").click(function () {
//     // Toggle the dropdown just below the clicked header
//     $(this).next(".jobs-filter-dropdown").toggleClass("hidden flex");
//     // Toggle the arrow icon in the clicked header
//     $(this)
//       .find(".arrow")
//       .toggleClass("ri-arrow-up-s-line ri-arrow-down-s-line");
//   });

//   $("#btn-filter").click(function () {
//     $("aside").toggleClass("hidden block");
//   });
//   $("#btn-apply-filter").click(function () {
//     $("aside").toggleClass("hidden block");
//   });


//   // Sidebar Toggle
//   $("#btn-open-sidebar").on("click", () => {
//     if ($("#sidebar").hasClass("hidden")) {
//       $("#sidebar").removeClass("hidden");
//     }
//   });

//   $("#btn-close-sidebar").on("click", () => {
//     if (!$("#sidebar").hasClass("#hidden")) {
//       $("#sidebar").addClass("hidden");
//     }
//   });


//   // Settings.html
//   const $profileTab = $("#my-profile-settings");
//   const $loginDetailsTab = $("#login-details-settings");
//   const $notificationTab = $("#notifications-settings");
//   const $btnProfileTab = $("#btn-my-profile");
//   const $btnLoginDetailsTab = $("#btn-login-details");
//   const $btnNotificationTab = $("#btn-notifications");

//   const hiddenClass = "hidden";
//   const activeClass = "active";

//   function toggleActiveTab(showTab, ...hideTabs) {
//     showTab.removeClass(hiddenClass);
//     hideTabs.forEach((tab) => tab.addClass(hiddenClass));
//   }

//   function setActiveButton(activeButton, ...inactiveButtons) {
//     activeButton.addClass(activeClass);
//     inactiveButtons.forEach((button) => button.removeClass(activeClass));
//   }

//   $btnProfileTab.on("click", () => {
//     toggleActiveTab($profileTab, $loginDetailsTab, $notificationTab);
//     setActiveButton($btnProfileTab, $btnLoginDetailsTab, $btnNotificationTab);
//   });

//   $btnLoginDetailsTab.on("click", () => {
//     toggleActiveTab($loginDetailsTab, $profileTab, $notificationTab);
//     setActiveButton($btnLoginDetailsTab, $btnProfileTab, $btnNotificationTab);
//   });

//   $btnNotificationTab.on("click", () => {
//     toggleActiveTab($notificationTab, $profileTab, $loginDetailsTab);
//     setActiveButton($btnNotificationTab, $btnProfileTab, $btnLoginDetailsTab);
//   });

//   // Toggle password
//   $(".toggle-password").on("click", function () {
//     const $input = $(this).siblings(".txt-password");

//     // Toggle the type attribute
//     if ($input.attr("type") === "password") {
//       $input.attr("type", "text");
//       $(this).text("Hide");
//     } else {
//       $input.attr("type", "password");
//       $(this).text("Show");
//     }
//   });

// });


// Get DOM Elements
const domElements = {
  toggleMenuOpenButton: document.getElementById("toggleOpen"),
  toggleMenuCloseButton: document.getElementById("toggleClose"),
  collapsibleMenu: document.getElementById("collapseMenu"),
  profileAvatarButton: document.getElementById("avatarButton"),
  userDropdownMenu: document.getElementById("userDropdown"),
  passwordField: document.getElementById("password"),
  confirmPasswordField: document.getElementById("confirmPassword"),
  form: document.querySelector("form"),
  sidebar: document.getElementById("sidebar"),
  btnOpenSidebar: document.getElementById("btn-open-sidebar"),
  btnCloseSidebar: document.getElementById("btn-close-sidebar"),
  btnFilter: document.getElementById("btn-filter"),
  btnApplyFilter: document.getElementById("btn-apply-filter"),
  profileTab: document.getElementById("my-profile-settings"),
  loginDetailsTab: document.getElementById("login-details-settings"),
  notificationsTab: document.getElementById("notifications-settings"),
  btnProfileTab: document.getElementById("btn-my-profile"),
  btnLoginDetailsTab: document.getElementById("btn-login-details"),
  btnNotificationTab: document.getElementById("btn-notifications"),
  jobFilterHeaders: document.querySelectorAll(".jobs-filter"),
};

// Utility Functions
const elementExists = (element) => element !== null && typeof element !== "undefined";

const toggleVisibility = (element) => {
  if (elementExists(element)) {
    element.style.display = element.style.display === "none" ? "block" : "none";
  }
};

const toggleClass = (element, className) => {
  if (elementExists(element)) {
    element.classList.toggle(className);
  }
};

// Setup Toggle Menu Visibility
const setupMenuToggleButtons = () => {
  const { toggleMenuOpenButton, toggleMenuCloseButton, collapsibleMenu } = domElements;

  if (elementExists(toggleMenuOpenButton) && elementExists(toggleMenuCloseButton)) {
    toggleMenuOpenButton.addEventListener("click", () => toggleVisibility(collapsibleMenu));
    toggleMenuCloseButton.addEventListener("click", () => toggleVisibility(collapsibleMenu));
  }
};

// Setup Profile Dropdown Toggle
const setupProfileDropdownToggle = () => {
  const { profileAvatarButton, userDropdownMenu } = domElements;

  if (elementExists(profileAvatarButton)) {
    profileAvatarButton.addEventListener("click", () => {
      toggleClass(userDropdownMenu, "hidden");
    });
  }
};

// Setup Password Validation
const setupPasswordValidation = () => {
  const { form, passwordField, confirmPasswordField } = domElements;

  if (elementExists(form) && elementExists(passwordField) && elementExists(confirmPasswordField)) {
    form.addEventListener("submit", (event) => {
      const password = passwordField.value.trim();
      const confirmPassword = confirmPasswordField.value.trim();

      if (password !== confirmPassword) {
        alert("Passwords do not match!");
        event.preventDefault();
      }
    });
  }
};

// Sidebar Toggle
const setupSidebarToggle = () => {
  const { btnOpenSidebar, btnCloseSidebar, sidebar } = domElements;

  if (elementExists(btnOpenSidebar)) {
    btnOpenSidebar.addEventListener("click", () => {
      sidebar.classList.remove("hidden");
    });
  }

  if (elementExists(btnCloseSidebar)) {
    btnCloseSidebar.addEventListener("click", () => {
      sidebar.classList.add("hidden");
    });
  }
};

// Job Filter Dropdown Toggle
const setupJobFilterToggle = () => {
  const { jobFilterHeaders } = domElements;

  jobFilterHeaders.forEach((header) => {
    header.addEventListener("click", () => {
      const dropdown = header.nextElementSibling;
      const arrowIcon = header.querySelector(".arrow");

      if (elementExists(dropdown) && elementExists(arrowIcon)) {
        toggleClass(dropdown, "hidden");
        toggleClass(dropdown, "flex");
        toggleClass(arrowIcon, "ri-arrow-up-s-line");
        toggleClass(arrowIcon, "ri-arrow-down-s-line");
      }
    });
  });
};

// Filter Buttons Toggle
const setupFilterButtons = () => {
  const { btnFilter, btnApplyFilter } = domElements;

  if (elementExists(btnFilter)) {
    btnFilter.addEventListener("click", () => {
      toggleClass(document.querySelector("aside"), "hidden");
      toggleClass(document.querySelector("aside"), "block");
    });
  }

  if (elementExists(btnApplyFilter)) {
    btnApplyFilter.addEventListener("click", () => {
      toggleClass(document.querySelector("aside"), "hidden");
      toggleClass(document.querySelector("aside"), "block");
    });
  }
};

// Tab Navigation
const setupTabNavigation = () => {
  const { profileTab, loginDetailsTab, notificationsTab, btnProfileTab, btnLoginDetailsTab, btnNotificationTab } = domElements;

  const hiddenClass = "hidden";
  const activeClass = "active";

  const toggleTab = (activeTab, activeButton, ...inactiveTabsAndButtons) => {
    activeTab.classList.remove(hiddenClass);
    activeButton.classList.add(activeClass);

    inactiveTabsAndButtons.forEach(({ tab, button }) => {
      tab.classList.add(hiddenClass);
      button.classList.remove(activeClass);
    });
  };

  if (elementExists(btnProfileTab)) {
    btnProfileTab.addEventListener("click", () =>
      toggleTab(profileTab, btnProfileTab, { tab: loginDetailsTab, button: btnLoginDetailsTab }, { tab: notificationsTab, button: btnNotificationTab })
    );
  }

  if (elementExists(btnLoginDetailsTab)) {
    btnLoginDetailsTab.addEventListener("click", () =>
      toggleTab(loginDetailsTab, btnLoginDetailsTab, { tab: profileTab, button: btnProfileTab }, { tab: notificationsTab, button: btnNotificationTab })
    );
  }

  if (elementExists(btnNotificationTab)) {
    btnNotificationTab.addEventListener("click", () =>
      toggleTab(notificationsTab, btnNotificationTab, { tab: profileTab, button: btnProfileTab }, { tab: loginDetailsTab, button: btnLoginDetailsTab })
    );
  }
};

// Toggle Password Visibility
const setupPasswordToggle = () => {
  const togglePasswordButtons = document.querySelectorAll(".toggle-password");

  togglePasswordButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const passwordField = button.previousElementSibling; // Assuming the password input is before the button
      if (passwordField && passwordField.type === "password") {
        passwordField.type = "text";
        button.textContent = "Hide";
      } else if (passwordField) {
        passwordField.type = "password";
        button.textContent = "Show";
      }
    });
  });
};

// Initialize Event Listeners
const initializeEventListeners = () => {
  setupMenuToggleButtons();
  setupProfileDropdownToggle();
  setupPasswordValidation();
  setupSidebarToggle();
  setupJobFilterToggle();
  setupFilterButtons();
  setupTabNavigation();
  setupPasswordToggle();

};

// Run Setup on DOMContentLoaded
document.addEventListener("DOMContentLoaded", initializeEventListeners);


