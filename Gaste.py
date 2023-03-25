class Gast:
    def __init__(self, nachname, vorname):
        self.nachname = nachname
        self.vorname = vorname

    def aktualisierung_nachname(self, neue_name):
        self.nachname = neue_name                       #Der Nachname von dem Gaste wird aktualisiert

    def __str__(self):
        return f'First name: {self.vorname} -- Last name: {self.nachname}'