import random

class Player():
    def __init__(self, name):
        self.cards = []
        self.name = name
        self.numCardsToTrade = 0

    def chooseNumCardsToTrade(self):
        """
        Determine how many cards to trade this round
        :return: a random number between 1 and max
        """
        self.numCardsToTrade = random.randint(1, len(self.cards))
        return self.numCardsToTrade

    def getRandomCardsToTrade(self, numCards):
        """
        Removes a number of cards from the player and returns the list
        :param numCards: number of cards to remove from the player
        :return: a list of the cards removed
        """
        tradeCards = []
        random.shuffle(self.cards)
        for card in range(numCards):
            tradeCards.append(self.cards.pop())
        return tradeCards

    def addCards(self, cards):
        """
        Give cards to this player
        :param cards: a list of the cards to assign to this player
        :return: None
        """
        for card in cards:
            self.cards.append(card)

    def getCompleteTandas(self, tandaSize=4):
        """
        Return a list of all the complete tandas a player has.  A tanda is a set of
        songs whose composer and genre all match.
        :param tandaSize: how many matching songs make up a tanda
        :return: a list of composer/genre combinations that make up a tanda
        """
        tandas = []
        comboHistogram = {}
        for card in self.cards:
            combo = (card.composer, card.genre)
            if (not comboHistogram.has_key(combo)):
                comboHistogram[combo] = 0
            comboHistogram[combo] += 1

        for combo, count in comboHistogram.iteritems():
            if count >= tandaSize:
                tandas.append(combo)
        return tandas

    def hasTanda(self, tandaSize=4):
        """
        Determine whether a player has a tanda in his hand
        :param tandaSize: how many matching songs make up a tanda
        :return: True or False
        """
        return len(self.getCompleteTandas(tandaSize)) > 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return "%s (trading: %s)" % (self.name, self.numCardsToTrade)
