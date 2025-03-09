import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given an absolute path for a Unix-style file system, which always begins with a
        slash '/'. Your task is to transform this absolute path into its simplified canonical path.

        The rules of a Unix-style file system are as follows:

        - A single period '.' represents the current directory.
        - A double period '..' represents the previous/parent directory.
        - Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
        - Any sequence of periods that does not match the rules above should be treated as a valid
            directory or file name. For example, '...' and '....' are valid directory or file
            names.

        The simplified canonical path should follow these rules:

        - The path must start with a single slash '/'.
        - Directories within the path must be separated by exactly one slash '/'.
        - The path must not end with a slash '/', unless it is the root directory.
        - The path must not have any single or double periods ('.' and '..') used to denote current
            or parent directories.

        Return the simplified canonical path.

    Constraints:
        1 <= path.length <= 3000
        path consists of English letters, digits, period '.', slash '/' or '_'.
        path is a valid absolute Unix path.

    """

    def simplify_path(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()

            elif part != "." and part != "":
                stack.append(part)

        return "/" + "/".join(stack)

    def simplify_path_bad(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        temp = ""
        ans = ""
        i = 0

        while i < len(path):
            if stack and stack[-1] == "/" and path[i] != "/":
                while i < len(path) and path[i] != "/":
                    temp += path[i]
                    stack.append(path[i])
                    i += 1

                if temp == ".":
                    if stack:
                        stack.pop()
                    else:
                        stack.append("/")

                elif temp == "..":
                    while stack and stack[-1] != "/":
                        stack.pop()

                    if stack:
                        stack.pop()

                    while stack and stack[-1] != "/":
                        stack.pop()

                temp = ""

            elif stack and stack[-1] == "/" and path[i] == "/":
                i += 1
            else:
                stack.append(path[i])
                i += 1

        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
        elif not stack:
            stack.append("/")

        return ans.join(stack)


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = (
        "./data_structures_and_algorithms/stacks_and_queues/1_simplify_path/input.json"
    )

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: path = {item['path']}")
        output = solution.simplify_path(item["path"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
