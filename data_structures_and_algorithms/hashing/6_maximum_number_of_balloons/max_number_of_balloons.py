import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string text, you want to use the characters of text to form as many instances
        of the word "balloon" as possible.

        You can use each character in text at most once. Return the maximum number of
        instances that can be formed.

    Constraints:
        1 <= text.length <= 10^4
        text consists of lower case English letters only.

    """

    def max_number_of_balloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        from collections import defaultdict
        from collections import Counter

        balloon = Counter("balloon")
        count = defaultdict(int)

        for letter in text:
            if letter in balloon:
                count[letter] += 1

        for letter in balloon:
            if count[letter] == 0:
                return 0
            else:
                count[letter] //= balloon[letter]

        return min(count.values())


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/6_maximum_number_of_balloons/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: text = {item['text']}")
        output = solution.max_number_of_balloons(item["text"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")
        test(output, item["expected"])


if __name__ == "__main__":
    main()
