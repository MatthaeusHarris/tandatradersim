class Card():
    def __init__(self, composer, genre, title):
        self.composer = composer
        self.genre = genre
        self.title = title

    def __repr__(self):
        return "%s by %s (%s)" % (self.title, self.composer, self.genre)

    def __str__(self):
        return "%s by %s (%s)" % (self.title, self.composer, self.genre)

class Cards():
    def __init__(self, composerList, genreList, songsPerCombo):
        self.cards = []
        for composer in composerList:
            for genre in genreList:
                for song in range(songsPerCombo):
                    self.cards.append(Card(composer, genre, "%s %s" % (genre.capitalize(),
                                                                       song + 1)))


