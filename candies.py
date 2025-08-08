"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings. You are giving candies to these children subjected to the following requirements: Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. Return the minimum number of candies you need to have to distribute the candies to the children.

Example
Example 1:**bold text**
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104
"""

from typing import List, Tuple

class CandiesCalculator():
    @staticmethod
    def candies_distribution(ratings: List) -> Tuple[List, int]:
        if len(ratings) == 1:
            distribution = [1]
        
        else:

            distribution = [1] * len(ratings)
            
            for i in range(len(ratings)):
                actual = ratings[i]
                if i == 0:
                    left = 0
                    right = ratings[i+1]
                elif i < len(ratings)-1:
                    right = ratings[i+1]
                    left = ratings[i-1]
                else:
                    right = 0
                    left = ratings[i-1]
                if actual <= left and actual >= right:
                    if right != 0:
                        distribution[i] = 2
                        distribution[i-1] = 3
                        distribution[i+1] = 1
                if actual >= left and actual >= right:
                    if right != 0:
                        distribution[i] = 2
                        distribution[i-1] = 1
                        distribution[i+1] = 1
                    else:
                        distribution[i] = distribution[i-1] + 1
                if actual >= left and actual <= right:
                    if left != 0:
                        distribution[i+1] = 3
                        distribution[i] = 2
                    else:
                        distribution[i+1] = distribution[i] + 1

        return {"distribution": distribution, "min_candies": sum(distribution)}
    
    @staticmethod
    def candy(ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        # Iterate from left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        total_candies = candies[n - 1]
        import pdb
        pdb.set_trace()
        # Iterate from right to left and update candies
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
            total_candies += candies[i]

        return total_candies
            

if __name__ == "__main__":
    print(CandiesCalculator.candy([2,0,3,4,1]))
    print(CandiesCalculator.candies_distribution([3,2]))
    print(CandiesCalculator.candies_distribution([1]))
    print(CandiesCalculator.candies_distribution([1,2,3]))
    print(CandiesCalculator.candies_distribution([2,3]))
    print(CandiesCalculator.candies_distribution([3,2,3]))
    CandiesCalculator.candies_distribution([1,2,0])