/**
 * Tailwind CSS Configuration File
 * This file contains a minimal config customized for a Django project.
 */

module.exports = {
  content: [
    /**
     * Paths to Django template files where Tailwind CSS classes are used.
     * Adjust these paths based on your project's structure.
     */
    "../templates/**/*.html", // Templates in the theme app
    "../../templates/**/*.html", // Main templates directory
    "../../**/templates/**/*.html", // Templates in other apps
  ],
  theme: {
    extend: {
      /**
       * Custom colors for your project.
       * Make sure these are correctly defined and used in your templates.
       */
      colors: {
        primary: '#ffffff',    // White background
        secondary: '#333333',  // Dark gray text
        green: '#26ae61',      // Green color for buttons, etc.
        darkgreen: '#11a652',  // Dark green for hover or accent
      },
    },
  },
  plugins: [
    /**
     * Plugins for additional Tailwind functionality.
     */
    require("@tailwindcss/forms"), // Minimal styling for forms
    require("@tailwindcss/typography"), // Typography plugin for rich text
    require("@tailwindcss/aspect-ratio"), // Utilities for aspect ratios
  ],
};
