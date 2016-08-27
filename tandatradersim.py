import game

numPlayers = 60
numComposers = 6 # Max 16
songsPerCombo = 20
numCardsPerPlayer = 6
dances = 20
simulations = 1000
results = []

for i in range(0,simulations):
    g = game.Game(numPlayers=numPlayers,
                  numComposers=numComposers,
                  songsPerCombo=songsPerCombo,
                  numCardsPerPlayer=numCardsPerPlayer)

    tandasFound = g.runGame(iterations=dances)
    results.append(tandasFound)
    # print "Run=%s tandasFound=%s" % (i, tandasFound)
average = reduce(lambda x, y: x + y, results) / len(results)
failures = len(filter(lambda x: x == 0, results))
failureRate = (failures+0.0)/simulations
print "Final results:"
print "numPlayers = %s" % numPlayers
print "numComposers = %s" % numComposers
print "songsPerCombo = %s" % songsPerCombo
print "numCardsPerPlayer = %s" % numCardsPerPlayer
print "dances = %s" % dances
print "simulations = %s" % simulations
print "average number of tandas found: %s" % average
print "number of runs with zero tandas found: %s" % failures
print "failure rate: %s" % failureRate