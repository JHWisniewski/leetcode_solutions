import json

class Solution(object):
    """
    Description:
        There is a biker going on a road trip. The road trip consists of n + 1 points at different 
        altitudes. The biker starts his trip on point 0 with altitude equal 0.

        You are given an integer array gain of length n where gain[i] is the net gain in altitude 
        between points i and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

    Constraints:
        n == gain.length
        1 <= n <= 100
        -100 <= gain[i] <= 100

    """
    def largest_altitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        i, curr, ans = 0, 0, 0

        while i < len(gain):
            curr += gain[i]
            ans = max(ans, curr)
            i += 1

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    path = './data_structures_and_algorithms/arrays_and_strings/addtl_probs/1732_find_the_highest_altitude/input.json'

    with open(path, encoding = "utf-8") as f:
        data = json.loads(f.read())

    for item in data:
        print(f"Input: gain = {item['gain']}")
        output = solution.largest_altitude(item['gain'])
        print(f"Output: {output}")
        print(f"Expected Output: {item['expected']}")

        if output == item['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
