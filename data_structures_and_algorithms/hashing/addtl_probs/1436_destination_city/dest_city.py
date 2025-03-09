import json
from lib.test import test


class Solution(object):
    """
    Description:
        You are given the array paths, where paths[i] = [cityA[i], cityB[i]] means there exists
        a direct path going from cityA[i] to cityB[i]. Return the destination city, that is, the
        city without any path outgoing to another city.

        It is guaranteed that the graph of paths forms a line without any loop, therefore, there
        will be exactly one destination city.

    Constraints:
        1 <= paths.length <= 100
        paths[i].length == 2
        1 <= cityA[i].length, cityB[i].length <= 10
        cityA[i] != cityB[i]
        All strings consist of lowercase and uppercase English letters and the space character.

    """

    def dest_city(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        travel = {}

        for point_a, point_b in paths:
            if point_a not in travel:
                travel[point_a] = point_b

        for depart in travel:
            if travel[depart] not in travel:
                return travel[depart]


def main():
    # Setup of solution with LeetCode example input
    solution = Solution()
    path = "./data_structures_and_algorithms/hashing/addtl_probs/1436_destination_city/input.json"

    with open(path, encoding="utf-8") as file:
        data = json.load(file)

    for item in data:
        print(f"Input: paths = {item['paths']}")
        output = solution.dest_city(item["paths"])
        test(output, item["expected"])


if __name__ == "__main__":
    main()
