import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the
        order of characters. No two characters may map to the same character, but a character may
        map to itself.

    Constraints:
        1 <= s.length <= 5 * 10^4
        t.length == s.length
        s and t consist of any valid ascii character.

    """

    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_iso, t_iso = {}, {}

        for i in range(len(s)):
            if s[i] in s_iso:
                if s_iso[s[i]] != t[i]:
                    return False
            else:
                s_iso[s[i]] = t[i]

            if t[i] in t_iso:
                if t_iso[t[i]] != s[i]:
                    return False
            else:
                t_iso[t[i]] = s[i]

        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/205_isomorphic_strings/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: s = {item['s']}, t = {item['t']}")
        output = solution.is_isomorphic(item["s"], item["t"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
