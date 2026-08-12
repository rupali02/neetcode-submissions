class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for amt in range(1, amount+1):
            for coin in coins:
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1+dp[amt-coin])

        return -1 if dp[amount] == float('inf') else dp[amount]
        