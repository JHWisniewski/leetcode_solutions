import json
from lib.test import test


class Solution(object):
    """
    Description:
        A pangram is a sentence where every letter of the English alphabet appears at least once.

        Given a string sentence containing only lowercase English letters, return true if sentence
        is a pangram, or false otherwise.

    Constraints:
        1 <= sentence.length <= 1000
        sentence consists of lowercase English letters.

    """

    def check_if_pangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        import string

        letters = set(string.ascii_lowercase)
        s_letters = set(sentence)

        return s_letters == letters


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/1_check_if_the_sentence_is_pangram/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: sentence = {item['sentence']}")
        output = solution.check_if_pangram(item["sentence"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
