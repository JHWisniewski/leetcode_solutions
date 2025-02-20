import json


class Solution(object):
    """
    Description:
        You are given an integer array cards where cards[i] represents
        the value of the ith card. A pair of cards are matching if the
        cards have the same value.

        Return the minimum number of consecutive cards you have to pick up
        to have a pair of matching cards among the picked cards. If it is
        impossible to have matching cards, return -1.

    Constraints:
        1 <= cards.length <= 10^5
        0 <= cards[i] <= 10^6

    """

    def minimum_card_pickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        count = {}
        mins = []

        for i, c in enumerate(cards):
            if c not in count:
                count[c] = i
            else:
                mins.append(i - count[c] + 1)
                count[c] = i

        if mins:
            return min(mins)
        return -1


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/2260_minimum_consecutive_cards_to_pick_up/input.json"

    with open(path, encoding="utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: cards = {item['cards']}")
        output = solution.minimum_card_pickup(item["cards"])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item["expected"]:
            print("PASS")
        else:
            print("FAIL")
        print()


if __name__ == "__main__":
    main()
