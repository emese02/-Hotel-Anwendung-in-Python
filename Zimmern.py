class Zimmer:
    def __init__(self, nummer, nr_Gasten, preis, farbe, meerblick):
        self.nummer = nummer
        self.nr_gasten = nr_Gasten
        self.preis = preis
        self.farbe = farbe
        self.meerblick = meerblick

    def aktualisieren_preis(self, neue_preis):
        self.preis = neue_preis                     #der Preis der Zimmer wird aktualisiert mit den neuen Preis

    def __str__(self):
        return f'Number: {self.nummer} -- Nr. guests: {self.nr_gasten} -- Price: {self.preis} -- Color: {self.farbe} -- Sea-view: {self.farbe} -- Sea-view: {self.meerblick}'

    def __eq__(self, other):
        return self.nummer == other.nummer