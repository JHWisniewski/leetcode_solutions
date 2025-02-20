# LeetCode and Me

interview_prep_fun = LeetCode(python, ...)

## Links to LeetCode's Crash Courses

[Home Page](https://leetcode.com/explore/)

[Data Structures and Algorithms](https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/)

## Useful Info

### Linters and Formatters Used

[Pylint](https://github.com/pylint-dev/pylint)

[Black](https://github.com/psf/black)

### Python Custom Modules

For use of a custom module like:
```python 
from my_lib.my_file import my_function
```

 - Example from reverse_words.py: 
   ```python 
   from lib.reverse_string import reverse_string
   ```

You need to adjust some environment stuff.  For me personally using Windows with VS Code and Python, I had
to do the following:

   1. Create .env at root directory with:
      ```python
      PYTHONPATH = { YOUR WORKSPACE FOLDER }
      ```

   2. Adjust VS Code's 'PROJECT'.code-workspace file's settings JSON with:
      ```json
      "terminal.integrated.env.windows": {
         "PYTHONPATH": "${workspaceFolder};"
      },
      ```

## Micellaneous Items

### Project Tree

[The workspace](project_tree.md) (so far)...
