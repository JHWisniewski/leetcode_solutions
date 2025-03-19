import json
from lib.test import test


class StockSpanner(object):
    """
    Description:
        Design an algorithm that collects daily price quotes for some stock and returns the span of
        that stock's price for the current day.

        The span of the stock's price in one day is the maximum number of consecutive days
        (starting from that day and going backward) for which the stock price was less than or
        equal to the price of that day.

        For example, if the prices of the stock in the last four days is [7,2,1,2] and the price of
        the stock today is 2, then the span of today is 4 because starting from today, the price of
        the stock was less than or equal 2 for 4 consecutive days.

        Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the
        stock today is 8, then the span of today is 3 because starting from today, the price of the
        stock was less than or equal 8 for 3 consecutive days.

    Constraints:
        1 <= price <= 10^5
        At most 10^4 calls will be made to next.

    """

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1

        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]

        self.stack.append([price, ans])

        return ans


def main():
    # Setup of solution with LeetCode example input
    path = "./data_structures_and_algorithms/stacks_and_queues/5_online_stock_span/input.json"
    output = [None]

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input:\n{item['functions']}\n{item['parameters']}")
        solution = StockSpanner()

        for i in range(1, len(item["parameters"])):
            output.append(solution.next(item["parameters"][i][0]))

        test(output, item["expected"])


if __name__ == "__main__":
    main()
