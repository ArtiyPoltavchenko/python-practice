module.exports = {
  rules: {
    "type-enum": [2, "always", ["ADD", "FIX", "CHANGE", "REMOVE", "REFACTOR", "DOCS", "TEST", "MERGE"]],
    "type-case": [2, "always", "upper-case"], // Forces the type to be uppercase
    "type-empty": [2, "never"], // Prevents the type from being empty
    "subject-empty": [2, "never"], // Ensures the subject is not empty
    "subject-max-length": [2, "always", 50], // Limits the subject to 50 characters
    "header-max-length": [2, "always", 50], // Limits the full header (type + subject) to 50 characters
    "subject-case": [2, "always", "sentence-case"], // Ensures the first letter of the subject is capitalized
    "subject-full-stop": [2, "never", "."], // Ensures no period at the end of the subject
    "header-full-stop": [2, "never", "."], // Ensures no period at the end of the header
    "body-leading-blank": [2, "always"], // Ensures a blank line between the subject and body
  }
};
