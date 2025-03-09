import json
from lib.test import test


class Solution(object):
    """
    Description:
        Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one
        unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D
        plane and walk on the path specified by path.

        Return true if the path crosses itself at any point, that is, if at any time you are on a
        location you have previously visited. Return false otherwise.

    Constraints:
        1 <= path.length <= 10^4
        path[i] is either 'N', 'S', 'E', or 'W'.

    """

    def is_path_crossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        moves = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}

        seen = set()
        x, y = 0, 0

        seen.add((x, y))

        for move in path:
            dx, dy = moves[move]
            x += dx
            y += dy

            if (x, y) in seen:
                return True

            seen.add((x, y))

        return False


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/1496_path_crossing/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: path = {item['path']}")
        output = solution.is_path_crossing(item["path"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
