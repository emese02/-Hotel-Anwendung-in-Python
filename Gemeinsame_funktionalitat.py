def zeige_list(list):
    for elem in list:
        print(elem)

class Hotel:
    def __init__(self, gaste_list, zimmer_list, res_list):
        self.gaste_list = gaste_list
        self.zimmer_list = zimmer_list
        self.res_list = res_list


    def hinfugen_gast(self, gast):
        self.gaste_list.append(gast)                 #Die Gaste List wird erweitert

    def identifizieren_gast(self,g_nachname,g_vorname):
        l = len(self.gaste_list) - 1                # Wir gehen die Gast-List durch
        while l >= 0:
            if self.gaste_list[l].nachname == g_nachname and self.gaste_list[l].vorname == g_vorname:   # Wir liefern die Position den Gast
                return l
            else:
                l = l - 1
        return None

    def update_gast(self, index, neu):
        i = 0
        while i < len(self.res_list):
           j = 0
           while j < len(self.res_list[i].gaste_l):
               if self.res_list[i].gaste_l[j].nachname == self.gaste_list[index].nachname and self.res_list[i].gaste_l[j].vorname == self.gaste_list[index].vorname:
                    self.res_list[i].gaste_l[j].aktualisierung_nachname(neu)
               j += 1
           i += 1
        self.gaste_list[index].aktualisierung_nachname(neu)    #Wir verandern den alten Name von dem eingegeben Gast

    def loschen_gast(self, index):
        self.gaste_list.pop(index)                 #Wir entfernen den eingegeben Gast

    def zeigen_listen(self, kriterium):
        if kriterium == "gaste":                   #Wir zeigen Gast-Liste / Zimmer-Liste abhangig von dem Kriterium
            zeige_list(self.gaste_list)
        else:
            if kriterium == "zimmer":
                zeige_list(self.zimmer_list)


    def hinfugen_Zimmer(self, neue_z):
        self.zimmer_list.append(neue_z)            #Wir hinfugen einen neuen Zimmer

    def identifizieren_zimmer(self, nr):
        l = len(self.zimmer_list) - 1              #Wir gehen die Zimmer-List durch
        while l >= 0:
            if self.zimmer_list[l].nummer == nr:   #Wir liefern die Position von dem Zimmer mit die eingegeben Nummer
                return l
            else:
                l = l - 1
        return None

    def update_zimmer(self, index, neue_preis):
        self.zimmer_list[index].aktualisieren_preis(neue_preis)      #Wir aktualisieren den Preis

    def loschen_zimmer(self, index):
        self.zimmer_list.pop(index)                                 #Wir entfernen den eingegeben Gast

    def suchen(self, neu, nr):
        moglichkeit = []                                #Wir bilden eine List von den adäquaten Zimmern
        l = len(self.zimmer_list) - 1
        while l >= 0:
            if self.zimmer_list[l].nr_gasten >= nr:     #Der Anzahl von Gasten musst passieren
                cond = True                             #Wir nehmen an, dass der Zimmer in der gegeben Zeitraum frei ist
                for res in self.res_list:               #Wir gehen durch die Liste von Reservierungen und verifieren
                    if res.zimmer == self.zimmer_list[l] and res.zeitraum.kein_durchschnitt(neu) == False:
                        cond = False                    #die Bedingung ist nicht erfullt, es gibt uberlappen in Zeitperioden
                if cond is True:
                    moglichkeit.append(self.zimmer_list[l])     # falls es gibt keine Reservierung in den bestimmten
                                                                # Zeitperiod, wir fugen den Zimmer in der Liste
                                                                # "moglichkeit" hin
            l -= 1
        return moglichkeit

    def hinfugen_res(self,neue_res):
        self.res_list.append(neue_res)                          #Wir hinfugen neuen Reservierungen

    def filter(self, minimal, maximal, meerblick):
        bedingung_erfullt = []
        for zimmer in self.zimmer_list:            #Die eingegeben Bedingungen sollen passen
            if zimmer.preis >= minimal and zimmer.preis <= maximal and zimmer.meerblick == meerblick:
                bedingung_erfullt.append(zimmer)
        return bedingung_erfullt

    def aktuelle_reservierung(self, today_date):
        gasten = []
        for res in self.res_list:
            if today_date < res.zeitraum.zeit_abfahrt:
                #falls eine Reservation enthalt die heutige Datum, dann der entsprechende Reservierung ist aktuell
                for gast in res.gaste_l:
                    if gast not in gasten:
                        gasten.append(gast)
        return gasten

    def frei_zimmern(self,todays_date):
        frei_zimm = []
        for zimm in self.zimmer_list:
            id = zimm.nummer
            frei = True
            for res in self.res_list:
                if res.zimmer.nummer == id:
                   if todays_date >= res.zeitraum.zeit_ankunft  and todays_date <= res.zeitraum.zeit_abfahrt:
                       frei = False
                    #falls eine Reservation enthalt die heutige Datum, dann der entsprechende Zimmer ist nicht frei
            if frei == True:
                frei_zimm.append(zimm)
        return  frei_zimm