import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern
        and a non-empty word in s. Specifically:

        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word, and no two words map to the same letter.

    Constraints:
        1 <= pattern.length <= 300
        pattern contains only lower-case English letters.
        1 <= s.length <= 3000
        s contains only lowercase English letters and spaces ' '.
        s does not contain any leading or trailing spaces.
        All the words in s are separated by a single space.

    """

    def word_pattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        p_iso, w_iso = {}, {}
        words = s.split(" ")

        # Needed for bijection
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            if pattern[i] in p_iso:
                if p_iso[pattern[i]] != words[i]:
                    return False
            else:
                p_iso[pattern[i]] = words[i]

            if words[i] in w_iso:
                if w_iso[words[i]] != pattern[i]:
                    return False
            else:
                w_iso[words[i]] = pattern[i]

        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/290_word_pattern/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: pattern = {item['pattern']}, s = {item['s']}")
        output = solution.word_pattern(item["pattern"], item["s"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
