def coin_change(coins, amount) -> int:

    """
    goal is to find minimal amount of coins needed, an index i 

    in general, 0 coins if amount is 0, then 1 way, if 1 coins amount is either 1 or -1 

    EXAMPLE
    - coins = [1,2,5], amount = 11
        target = 3, how do we find the amount of coins which is minimal? 
        loop through coins and check for combination 
        
        e.g.    11 - 1 = 10,
                10 - 2 = 8,
                8 - 5 = 3,

                3 - 1 = 2,
                2 - 2 = 0 

                target this case is 5 but wrong since 

                11 = 1 + 5 + 5, which is minimal

    ALGORITHM: 
    - define a minimal coin array: 
        minimal for amount 0 is 0,
        minimal for amount 1 is 1,
        minimal for amount 2 is 1 if 2 is present or 1
        minimal for amount 3 is either 1,2 or 3 

    we see in the above a recursion where the minimal for each subsequent amount is the minimum of the previous or the previous + 1  (*)

    due to recursion, we use dynamic programming
    """

    dp = [amount + 1] * (amount + 1) 
    dp[0] = 0 

    for i in range(amount + 1):
        for coin in coins: 
            if coin <= i: #obviously, negative values are not allowed 
                dp[i] = min(dp[i], dp[i - coin] + 1) #implementation of *

    if dp[amount] == amount + 1: 
        return -1 
    

    return dp[amount]


coins = [1,2,5] 
amount = 11

print(coin_change(coins=coins, amount=amount))




