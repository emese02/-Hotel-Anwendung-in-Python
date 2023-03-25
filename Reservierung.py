class Zeitraum:
    def __init__(self, zeit_ankunft, zeit_abfahrt):
        self.zeit_ankunft = zeit_ankunft
        self.zeit_abfahrt = zeit_abfahrt

    def kein_durchschnitt(self, andere_period):
        """
        liefert True falls die zwei Perioden haben keinen Durchschnitt, also es gibt keine Uberlappen
        """
        if andere_period.zeit_ankunft > self.zeit_abfahrt or self.zeit_ankunft > andere_period.zeit_abfahrt:
            return True
        else:
            return False

    def __str__(self):
        return f'Arrival: {self.zeit_ankunft}, Departure: {self.zeit_abfahrt}'

class Reservierung:
    def __init__(self, gaste_l, zimmer, zeitraum):
        self.gaste_l = gaste_l
        self.zimmer = zimmer
        self.zeitraum = zeitraum



