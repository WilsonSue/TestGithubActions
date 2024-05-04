const globals = require("globals");

module.exports = {
  languageOptions: {
    ecmaVersion: 2022,
    sourceType: "module",
    globals: {
      ...globals.browser,
      myCustomGlobal: "readonly",
    },
  },
  rules: {
    semi: ["error", "always"],
  },
};
