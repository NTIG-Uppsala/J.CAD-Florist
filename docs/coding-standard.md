# Coding Standard

* Code and file names are written in English.
* Comments are written in English.
* Variable names and functions are written in camelCase.
* IDs and classes in HTML are written in camelCase.
* Classes in Python and JavaScript should be written in PascalCase.
* File names are defined using kebab-case.
* File names for test files are written in snake_case.
* Branch names in Git are written in camelCase.
* Functions should generally be short and have a specific purpose. If a function becomes very long (around more than 100 lines), consider whether it can be split into separate functions.
* Avoid global variables unless they are necessary.
* When possible in the language, apply data types for variables and return types for functions. This makes the code clearer and is a good rule to follow.

* Formatting
    * settings.json:
    ```json
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "prettier.tabWidth": 4,
    "prettier.bracketSameLine": true,
    "prettier.printWidth": 200,
    ```