import json
from lib.test import test
from collections import deque


class RecentCounter(object):
    """
    Description:
        You have a RecentCounter class which counts the number of recent requests within a certain
        time frame.

        Implement the RecentCounter class:

        RecentCounter() Initializes the counter with zero recent requests.

        int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
        and returns the number of requests that has happened in the past 3000 milliseconds
        (including the new request). Specifically, return the number of requests that have happened
        in the inclusive range [t - 3000, t].

        It is guaranteed that every call to ping uses a strictly larger value of t than the
        previous call.

    Constraints:
        1 <= t <= 10^9
        Each test case will call ping with strictly increasing values of t.
        At most 10^4 calls will be made to ping.

    """

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)


def main():
    # Setup of solution with LeetCode example input
    path = "./data_structures_and_algorithms/stacks_and_queues/addtl_probs/933_number_of_recent_calls/input.json"
    output = [None]

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        solution = RecentCounter()
        print(f"Input: operations = {item['operations']}")

        for i, o in enumerate(item["operations"][0]):
            if o == "ping":
                output.append(solution.ping(item["operations"][1][i][0]))

        test(output, item["expected"])


if __name__ == "__main__":
    main()
