coins = [200, 100, 50, 20, 10, 5, 2, 1]

def makeChange(amount, coins):
    counter = 0
    coins = sorted(coins, reverse=True)
    def generator(index, remaining):
        coin = coins[index]
        if index == 0:
            if remaining % coin == 0 : counter += 1
            return
        while remaining >= 0:
            generator(index - 1, remaining)
            remaining -= index
    generator(coins - 1, amount)
    return counter
