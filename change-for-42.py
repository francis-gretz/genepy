def countRecur(amount, coins, index, memo):
    # If amount is 0 then there is 1 solution
    # (do not include any coin)
    if amount == 0:
        return 1

    # 0 ways in the following two cases
    if amount < 0 or index == 0:
        return 0

    # If the subproblem is previously calculated then
    # simply return the result
    if memo[index - 1][amount] != -1:
        return memo[index - 1][amount]

    # count is amount of solutions
    #  - (i)  including coins[index-1]
    #  - (ii) excluding coins[index-1]
    i = countRecur(amount - coins[index - 1], coins, index, memo)
    ii = countRecur(amount, coins, index - 1, memo)

    memo[index - 1][amount] = i + ii

    return memo[index - 1][amount]


def changes(amount, coins):
    memo = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
    return countRecur(amount, coins, len(coins), memo)


res = changes(42, (1, 2, 5, 10, 20, 50, 100, 200, 500))
print(res)
