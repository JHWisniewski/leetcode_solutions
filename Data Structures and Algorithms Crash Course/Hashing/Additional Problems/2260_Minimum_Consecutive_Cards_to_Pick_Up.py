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
    def minimumCardPickup(self, cards):
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
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem Inputs/2260_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: cards = {object['cards']}")
        output = solution.minimumCardPickup(object['cards'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()