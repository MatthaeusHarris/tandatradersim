import card
import player
import random

composers = ["D'Arienzo", "Di Sarli", "Troilo", "Pugliese",
             "Calo", "DeAngelis", "Laurenz", "Biagi", "Tanturi",
             "Carabelli", "Firpo", "Fresedo", "De Caro", "Donato",
             "Canaro", "Rodriguez"]
genres = ["tango", "vals", "milonga"]

class Game():
    def __init__(self, numPlayers, numComposers, songsPerCombo, numCardsPerPlayer):
        if numComposers * len(genres) * songsPerCombo < numPlayers * numCardsPerPlayer:
            raise GameError("Not enough cards for the number of players")

        if numComposers > len(composers):
            raise GameError("Too many composers specified")

        self.numComposers = numComposers
        self.songsPerCombo = songsPerCombo
        self.numCardsPerPlayer = numCardsPerPlayer

        # Create players
        self.players = [player.Player("Player %s" % x) for x in range(0, numPlayers)]

        # Create cards
        selectedComposers = [composers[x] for x in range(0,numComposers)]
        self.cards = card.Cards(selectedComposers, genres, songsPerCombo)
        random.shuffle(self.cards.cards)

        # Assign cards to players
        for i, p in enumerate(self.players):
            p.addCards(self.cards.cards[i*numCardsPerPlayer:(i+1)*numCardsPerPlayer])

    def matchTradingPlayers(self):
        self.matchQueue = [[] for x in range(0,self.numCardsPerPlayer)]
        self.pairs = []
        for p in self.players:
            p.chooseNumCardsToTrade()

        for p in self.players:
            if len(self.matchQueue[p.numCardsToTrade-1]) > 0:
                self.pairs.append([p, self.matchQueue[p.numCardsToTrade-1].pop()])
            else:
                self.matchQueue[p.numCardsToTrade-1].append(p)

        return self.pairs

    def doTradeCards(self):
        for pair in self.pairs:
            player1 = pair[0]
            player2 = pair[1]
            tempCards = player1.getRandomCardsToTrade(player1.numCardsToTrade)
            player1.addCards(player2.getRandomCardsToTrade(player2.numCardsToTrade))
            player2.addCards(tempCards)

    def findTandas(self):
        tandasFound = 0
        for p in self.players:
            if p.hasTanda():
                tandasFound += 1
        return tandasFound

    def runGame(self, iterations):
        tandasFound = self.findTandas()
        for i in range(0,iterations):
            self.matchTradingPlayers()
            self.doTradeCards()
            tandasFound += self.findTandas()
        return tandasFound


class GameError(Exception):
    pass