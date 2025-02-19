import json

class Solution(object):
    """
    Description:
        You are given an integer array matches where matches[i] = [winner[i], loser[i]] indicates that the player 
        winner[i] defeated player loseri in a match.

        Return a list answer of size 2 where:

        answer[0] is a list of all players that have not lost any matches.
        answer[1] is a list of all players that have lost exactly one match.
        The values in the two lists should be returned in increasing order.

        Note:
            You should only consider the players that have played at least one match.
            
            The testcases will be generated such that no two matches will have the same outcome.

    Constraints:
        1 <= matches.length <= 10^5
        matches[i].length == 2
        1 <= winner[i], loser[i] <= 10^5
        winner[i] != loser[i]
        All matches[i] are unique.
        
    """
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        players = set()
        losses, wins = defaultdict(int), defaultdict(int)
        zero, one = [], []

        for match in matches:
            #Add players into players set
            if match[0] not in players:
                players.add(match[0])
            if match[1] not in players:
                players.add(match[1])

            #Tally wins and losses
            wins[match[0]] += 1
            losses[match[1]] += 1

        for player in players:
            if player not in losses:
                zero.append(player)
            elif losses[player] == 1:
                one.append(player)

        return [sorted(zero), sorted(one)]

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem-Inputs/4_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: matches = {object['matches']}")
        output = solution.findWinners(object['matches'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        if output == object['expected']:
            print("PASS")
        else:
            print("FAIL")
        print()

if __name__ == "__main__":
    main()