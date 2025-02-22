# LeetCode and Me

interview_prep_fun = LeetCode(python, ...)


## 1. Links to LeetCode's Crash Courses

- [Home Page](https://leetcode.com/explore/)
- [Data Structures and Algorithms](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/)


## 2. Useful Info

### A. Linters and Formatters Used

- [Pylint - VS Code Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.pylint)

   I recommend installing the VS Code extension for inline suggestions on current warnings.  It takes some tweaking to get your warnings right.

   That involves some annoying workspace adjustments to VS Code settings specifically that I will not elaborate on.

- [Pylint - CLI](https://github.com/pylint-dev/pylint)

   Run this directly in your root directory for a CLI-oriented experience.

   1. To install, run `pip install Pylint` (May be different for you!)

   2. Run `Pylint .` in your root directory and watch the magic

      - I got this running pretty well with my .pylintrc file.  You can see the contents in my repo with some comments on arguments.

- [pre-commit](https://pre-commit.com/)

   This interfaces directly with git to perform formatting before commits/pushes to a branch.

   1. Run `pip install pre-commit` in root directory (I am using PowerShell in VS Code, so yours may differ).

   2. Create .pre-commit-config.yaml in your root directory with the following (default) contents:
      ```yaml
      repos:
      -   repo: https://github.com/pre-commit/pre-commit-hooks
         rev: v2.3.0
         hooks:
         -   id: check-yaml
         -   id: end-of-file-fixer
         -   id: trailing-whitespace
      -   repo: https://github.com/psf/black
         rev: 22.10.0
         hooks:
         -   id: black
      ```

      - I would like to experiment with adding custom scripts.  It looks like the following will be applicable:
         ```yaml
         - repo: local
         hooks:
            - id: custom-script-file
               name: custom-script-file
               entry: relative/path/to/repo/root/check_pylint.sh
               language: script
               types: [python]
               pass_filenames: false
         ```

   3. Run `pre-commit install`

   4. You are done!  Now when you run `git commit -m "<YOUR MESSAGE>"` after staging files, you will have auto formatting performed on your code!

      - NOTE: If the formatters change files, you have to repeat your `git add -all` and `git commit -m "<YOUR MESSAGE>"` commands

- [Black](https://github.com/psf/black)

   Available as part of the recommended git hooks installed with pre-commit. (See pre-commit link)

### B. Python Custom Modules

For use of a custom module like:
```python
from my_lib.my_file import my_function
```

 - Example from reverse_words.py:
   ```python
   from lib.reverse_string import reverse_string
   ```

You need to adjust some environment stuff.  For me personally using Windows with VS Code and Python, I had to do the following:

   1. Create .env at the root directory with the following contents:
      ```python
      PYTHONPATH = { "<YOUR WORKSPACE FOLDER>" }
      ```

   2. Adjust VS Code's 'PROJECT'.code-workspace file's settings JSON with:
      ```json
      "terminal.integrated.env.windows": {
         "PYTHONPATH": "${workspaceFolder};"
      },
      ```

   3. Create a debug launch.json from the **Run and Debug** menu and change the following contents:
      ```json
      {
         "version": "0.2.0",
         "configurations": [
            {
                  "name": "Python: Module",
                  "type": "debugpy",
                  "request": "launch",
                  "module": "folder_structure.main",
                  "justMyCode": true
            },
            {
                  "name": "Python: Current File",
                  "type": "debugpy",
                  "request": "launch",
                  "program": "${file}",
                  "console": "integratedTerminal",
                  "env": {
                     "PYTHONPATH": "${workspaceRoot}"
                  },
                  "cwd": "${workspaceRoot}",
            }
         ]
      }
      ```

   You can now run python files as normal from the **Run Python File** button up top. To debug, you will need to go into the **Run and Debug** menu on the primary sidebar and ensure **Python: Current File** is selected.  Run from the play button there when needed. (Still looking into other options for this... VS Code, why?)


## 3. Micellaneous Items

### A. Project Tree

[The workspace](project_tree.md) (so far)...
