import json
from lib.test import test
from collections import deque


class MovingAverage(object):
    """
    Description:
        Given a stream of integers and a window size, calculate the moving average of all integers
        in the sliding window.

        Implement the MovingAverage class:

        MovingAverage(int size) Initializes the object with the size of the window size.

        double next(int val) Returns the moving average of the last size values of the stream.

    Constraints:
        1 <= size <= 1000
        -10^5 <= val <= 10^5
        At most 10^4 calls will be made to next.

    """

    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += val
        self.queue.append(val)

        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()

        average = float(self.total) / len(self.queue)

        return float(str(f"{average:.5f}"))


def main():
    # Setup of solution with LeetCode example input
    path = "./data_structures_and_algorithms/stacks_and_queues/3_moving_average_from_data_stream/input.json"
    output = [None]

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input:\n{item['functions']}\n{item['parameters']}")
        solution = MovingAverage(item["parameters"][0][0])

        for i in range(1, len(item["parameters"])):
            output.append(solution.next(item["parameters"][i][0]))

        test(output, item["expected"])


if __name__ == "__main__":
    main()
