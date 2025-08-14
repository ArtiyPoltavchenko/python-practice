#!/bin/bash

# Check if inside a Git repository
if [ ! -d ".git" ]; then
  echo "No .git directory found. Initializing a new Git repository..."
  git init
else
  echo ".git directory found. Proceeding with setup..."
fi

# Check if global Git user.name and user.email are set!
git_user_name=$(git config --global user.name)
git_user_email=$(git config --global user.email)

if [ -z "$git_user_name" ] || [ -z "$git_user_email" ]; then
  echo "Global Git user.name and/or user.email are not set. Please enter your credentials."

  # Ask for user credentials
  read -r -p "Enter your Git user.name: " git_user_name
  read -r -p "Enter your Git user.email: " git_user_email

  # Configure Git with the provided credentials globally
  git config --global user.name "$git_user_name"
  git config --global user.email "$git_user_email"
else
  echo "Global Git user.name and user.email are already set."
fi

# Step 1: Install Commitlint and Husky
echo "Installing Commitlint and Husky..."
npm install --save-dev @commitlint/config-conventional @commitlint/cli husky

# # Create commitlint.config.js file with rules
# echo "Creating commitlint.config.js..."
# cat <<EOL > commitlint.config.js
# module.exports = {
#   extends: ['@commitlint/config-conventional'],
#   rules: {
#     'header-max-length': [2, 'always', 50], // Limit subject line to 50 characters
#     'header-full-stop': [2, 'never', '.'], // Do not end the subject line with a period
#     'type-enum': [
#       2,
#       'always',
#       ['ADD', 'FIX', 'CHANGE', 'REMOVE', 'REFACTOR', 'DOCS', 'TEST', 'MERGE']
#     ],
#     'type-case': [2, 'always', 'upper-case'], // Allow only uppercase types
#     'subject-case': [2, 'always', 'sentence-case'], // Capitalize the first letter of the subject line
#     'subject-empty': [2, 'never'], // Subject line should not be empty
#     'subject-full-stop': [2, 'never', '.'], // Do not end the subject line with a period
#     'body-leading-blank': [2, 'always'], // Separate subject from body with a blank line
#     'body-max-line-length': [2, 'always', 72], // Limit body lines to 72 characters
#     'footer-leading-blank': [2, 'always'], // Separate body from footer with a blank line
#     'footer-max-line-length': [2, 'always', 72] // Limit footer lines to 72 characters
#   }
# };
# EOL

# Initialize Husky using husky-init
echo "Initializing Husky..."
npx husky-init && npm install -y

# Ensure .husky directory exists
mkdir -p .husky

# Step 4: Manually create the commit-msg hook
echo "Creating commit-msg hook..."
cat <<EOL > .husky/commit-msg
npx --no-install commitlint --edit "\$1"
EOL

# Make the commit-msg hook executable
chmod +x .husky/commit-msg

# Verify the hook was added
if [ -f .husky/commit-msg ]; then
    echo "Commitlint hook added successfully."
else
    echo "Failed to add Commitlint hook."
fi

# Step 5: Remove the pre-commit hook if it exists
if [ -f .husky/pre-commit ]; then
    echo "Removing pre-commit hook..."
    echo '' > .husky/pre-commit
fi

echo "Husky and Commitlint have been set up successfully."