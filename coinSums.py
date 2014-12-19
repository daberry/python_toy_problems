coins = [200, 100, 50, 20, 10, 5, 2, 1]
cache = {}

def makeChange(total, coins):
    counter = 0
    coins.sort()
    def generator(index, remainder):
        coin = coins[index]
        if index == 0:
            remainder % coin == 0 && counter += 1
            return
        while remainder >= 0:
            generator(index - 1, remainder)
            remainder -= coin
    generator(len(coins) - 1, total)
    return counter
