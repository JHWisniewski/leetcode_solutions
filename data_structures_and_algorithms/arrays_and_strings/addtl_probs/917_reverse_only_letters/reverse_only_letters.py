import json
import string
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string s, reverse the string according to the following rules:

        All the characters that are not English letters remain in the same position.

        All the English letters (lowercase or uppercase) should be reversed.

        Return s after reversing it.

    Constraints:
        1 <= s.length <= 100
        s consists of characters with ASCII values in the range [33, 122].
        s does not contain '\"' or '\\'.

    """

    def reverse_only_letters(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # Two pointers for reversing string
        ans = list(s)
        left = 0
        right = len(s) - 1
        letters = set(string.ascii_uppercase + string.ascii_lowercase)

        while left < right:
            if ans[left] != ans[right] and ans[left] not in letters:
                left += 1
            elif ans[left] != ans[right] and ans[right] not in letters:
                right -= 1
            else:
                temp = ans[left]
                ans[left] = ans[right]
                ans[right] = temp
                left += 1
                right -= 1

        # Convert list to str
        ans = "".join(ans)

        return ans


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/arrays_and_strings/addtl_probs/917_reverse_only_letters/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: s = {item['s']}")
        output = solution.reverse_only_letters(item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
