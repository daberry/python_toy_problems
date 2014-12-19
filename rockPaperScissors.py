plays = ['rock', 'paper', 'scissors']

def rps(rounds, plays):
    result = []
    playedSoFar = []
    def combinations(roundsToGo):
        if roundsToGo == 0:
            result.append(playedSoFar[0:1])
        for play in plays:
            playedSoFar.append(play)
            combinations(roundsToGo - 1)
            playedSoFar.pop()
    combinations(rounds)
    return result
