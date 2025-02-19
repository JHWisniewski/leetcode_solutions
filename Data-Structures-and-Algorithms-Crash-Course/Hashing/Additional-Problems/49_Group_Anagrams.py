import json

class Solution(object):
    """
    Description:
        Given an array of strings strs, group the anagrams together. 
        You can return the answer in any order.

    Constraints:
        1 <= strs.length <= 10^4
        0 <= strs[i].length <= 100
        strs[i] consists of lowercase English letters.
        
    """
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            word = "".join(sorted(s))
            groups[word].append(s)

        return list(groups.values())

def main():
    #Setup of solution with LeetCode example input
    solution = Solution()
    
    with open('./Problem-Inputs/49_Input.json') as f:
        JSON = json.loads(f.read())

    for object in JSON:
        print(f"Input: strs = {object['strs']}")
        output = solution.groupAnagrams(object['strs'])
        print(f"Output: {output}")
        print(f"Expected Output: {object['expected']}")

        print("Output sorted by LeetCode, ensure groups in each Output are equal.")
        print()

if __name__ == "__main__":
    main()