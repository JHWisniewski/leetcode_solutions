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
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        i = curr = ans = 0

        while i < len(gain):
            curr += gain[i]
            ans = max(ans, curr)
            i += 1

        return ans

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()

    with open('./Problem Inputs/1732_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: gain = {object['gain']}")
        output = solution.largestAltitude(object['gain'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()
        