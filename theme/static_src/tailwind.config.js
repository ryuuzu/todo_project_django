/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
	content: [
		/**
		 * HTML. Paths to Django template files that will contain Tailwind CSS classes.
		 */

		/*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
		"../templates/**/*.html",

		/*
		 * Main templates directory of the project (BASE_DIR/templates).
		 * Adjust the following line to match your project structure.
		 */
		"../../templates/**/*.html",

		/*
		 * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
		 * Adjust the following line to match your project structure.
		 */
		"../../**/templates/**/*.html",

		/**
		 * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
		 * patterns match your project structure.
		 */
		/* JS 1: Ignore any JavaScript in node_modules folder. */
		// '!../../**/node_modules',
		/* JS 2: Process all JavaScript files in the project. */
		// '../../**/*.js',

		/**
		 * Python: If you use Tailwind CSS classes in Python, uncomment the following line
		 * and make sure the pattern below matches your project structure.
		 */
		// '../../**/*.py'
	],
	theme: {
		extend: {
			dropShadow: {
				card: "0 0 0.75rem rgba(255, 255, 255, 0.2)",
			},

			fontFamily: {
				titleDisplay: ["Satisfy", "cursive"],
				sans: ["Inter", "sans-serif"],
			},
			minWidth: {
				40: "40%",
				"1/2": "50%",
				60: "60%",
			},
			maxWidth: {
				40: "40%",
				60: "60%",
			},
			minHeight: {
				"1/2": "50%",
				40: "40%",
				30: "30%",
			},
			boxShadow: {
				epic: "-5px -5px 10px rgba(33, 33, 43, 0.5),3px 3px 10px rgba(255, 255, 255, 0.5)",
			},
			colors: {
				pending: "#ffa500",
				completed: "#4aa24a",
				secondaryBlack: "#21212b",
				primaryBlack: "#181820",
				black: "#160526",
				"dark-purple": "#5b364b",
				indigo: "#6466a8",
				gold: "#faa50e",
				red: "#cf3b2e",
				lavender: "#d8ccd8",
			},
		},
	},
	plugins: [
		/**
		 * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
		 * for forms. If you don't like it or have own styling for forms,
		 * comment the line below to disable '@tailwindcss/forms'.
		 */
		require("@tailwindcss/forms"),
		require("@tailwindcss/typography"),
		require("@tailwindcss/line-clamp"),
		require("@tailwindcss/aspect-ratio"),
	],
};
