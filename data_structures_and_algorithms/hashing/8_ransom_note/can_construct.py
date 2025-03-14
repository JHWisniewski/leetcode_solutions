import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by
        using the letters from magazine and false otherwise.

        Each letter in magazine can only be used once in ransomNote.

    Constraints:
        1 <= ransomNote.length, magazine.length <= 10^5
        ransomNote and magazine consist of lowercase English letters.

    """

    def can_construct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        magazine_count = Counter(magazine)
        note_count = Counter(ransomNote)

        for letter in note_count:
            if (
                letter not in magazine_count
                or note_count[letter] > magazine_count[letter]
            ):
                return False

        return True


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/8_ransom_note/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(
            f"Input: ransomNote = {item['ransomNote']}, magazine = {item['magazine']}"
        )
        output = solution.can_construct(item["ransomNote"], item["magazine"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
