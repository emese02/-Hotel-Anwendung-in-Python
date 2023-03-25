from Zimmern import Zimmer
from Gaste import Gast
from Gemeinsame_funktionalitat import Hotel
from Reservierung import Reservierung, Zeitraum
import datetime

def test_aktualisieren_preis():
        zimm = Zimmer(13, 2, 100, "purple", "yes")
        zimm.aktualisieren_preis (150)
        assert zimm.preis == 150

def test_aktualisierung_nachname():
        gast = Gast("Lucescu", "Mirela")
        gast.aktualisierung_nachname("Muntean")
        assert gast.nachname == "Muntean"

def test_update_gast():
        gast0 = Gast("Lucescu", "Gabriela")
        gast1 = Gast("Lucescu", "Mirela")
        gast2 = Gast("Cadar", "Ioana")
        gast3 = Gast("Cozma", "Denis")
        zimm1 = Zimmer(13, 2, 100, "lila", "yes")
        zimm2 = Zimmer(14, 3, 150, "yellow", "no")
        date_A = Zeitraum(datetime.date(2022, 5, 13), datetime.date(2022, 6, 7))
        date_B = Zeitraum(datetime.date(2020, 6, 8), datetime.date(2021, 11, 11))
        date_C = Zeitraum(datetime.date(2021, 11, 30), datetime.date(2021, 12, 15))
        res1 = Reservierung([gast1, gast2, gast3], zimm2, date_A)
        res2 = Reservierung([gast1,gast2], zimm1, date_B)
        res3 = Reservierung([gast1,gast3], zimm2, date_C)
        hotel1 = Hotel([gast0, gast1, gast2], [zimm1, zimm2], [res1,res2,res3])
        hotel1.gaste_list[1].aktualisierung_nachname("Dragan")
        assert  hotel1.gaste_list[1].nachname == "Dragan"
        assert  hotel1.res_list[1].gaste_l[0].nachname == "Dragan"

def test_identifizieren_gast():
        gast0 = Gast("Cadar", "Ioana")
        gast1 = Gast("Lucescu", "Gabriela")
        gast2 = Gast("Lucescu", "Mirela")
        hotel1 = Hotel([gast0, gast1, gast2], [], [])
        gast_index = hotel1.identifizieren_gast("Lucescu","Gabriela")
        assert gast_index == 1

def test_hinfugen_gast():
        gast1 = Gast("Lucescu", "Gabriela")
        gast2 = Gast("Lucescu", "Mirela")
        hotel1 = Hotel([gast1, gast2], [],[])
        gast3 = Gast("Cadar", "Ioana")
        hotel1.hinfugen_gast(gast3)
        assert hotel1.gaste_list == [gast1, gast2, gast3]

def test_loschen_gast():
        gast0 = Gast("Lucescu", "Gabriela")
        gast1 = Gast("Lucescu", "Mirela")
        gast2 = Gast("Cadar", "Ioana")
        hotel1 = Hotel([gast0, gast1, gast2], [], [])
        hotel1.loschen_gast(1)
        assert hotel1.gaste_list == [gast0, gast2]

def test_hinfugen_zimmer():
        zimm1 = Zimmer(13, 2, 100, "lila", "yes")
        zimm2 = Zimmer(14, 3, 150, "yellow", "no")
        zimm3 = Zimmer(17, 4, 190, "pink", "yes")
        hotel1 = Hotel([], [zimm1, zimm2], [])
        hotel1.hinfugen_Zimmer(zimm3)
        assert hotel1.zimmer_list == [zimm1, zimm2, zimm3]

def test_identifizierien_zimmer():
        zimm0 = Zimmer(13, 2, 100, "lila", "yes")
        zimm1 = Zimmer(14, 3, 150, "yellow", "no")
        zimm2 = Zimmer(17, 4, 190, "pink", "yes")
        hotel1 = Hotel([], [zimm0, zimm1, zimm2], [])
        assert hotel1.identifizieren_zimmer(14) == 1
        assert  hotel1.identifizieren_zimmer(19) == None

def test_update_zimmer():
        zimm0 = Zimmer(13, 2, 100, "lila", "yes")
        zimm1 = Zimmer(14, 3, 150, "yellow", "no")
        zimm2 = Zimmer(17, 4, 190, "pink", "yes")
        hotel1 = Hotel([], [zimm0, zimm1, zimm2], [])
        hotel1.zimmer_list[1].aktualisieren_preis(200)
        assert hotel1.zimmer_list[1].preis == 200

def test_loschen_zimmer():
        zimm0 = Zimmer(13, 2, 100, "lila", "yes")
        zimm1 = Zimmer(14, 3, 150, "yellow", "no")
        zimm2 = Zimmer(17, 4, 190, "pink", "yes")
        hotel1 = Hotel([], [zimm0, zimm1, zimm2], [])
        hotel1.zimmer_list.pop(1)
        assert  hotel1.zimmer_list == [zimm0, zimm2]

def test_kein_durchschnitt():
        A_ankunft = datetime.date(2021, 5, 15)
        A_abfahrt = datetime.date(2021, 5, 30)
        B_ankunft = datetime.date(2021, 5, 31)
        B_abfahrt = datetime.date(2021, 6, 10)
        date_A = Zeitraum(A_ankunft, A_abfahrt)
        date_B = Zeitraum(B_ankunft, B_abfahrt)
        assert date_A.kein_durchschnitt(date_B) == True
        C_ankunft = datetime.date(2021, 5, 15)
        C_abfahrt = datetime.date(2021, 5, 30)
        D_ankunft = datetime.date(2021, 5, 28)
        D_abfahrt = datetime.date(2021, 6, 10)
        date_C = Zeitraum(C_ankunft, C_abfahrt)
        date_D = Zeitraum(D_ankunft, D_abfahrt)
        assert date_C.kein_durchschnitt(date_D) == False

def test_aktuelle_reservierung():
        gast1 = Gast("Sandru", "Gabriel")
        gast2 = Gast("Criste", "Cosmin")
        gast3 = Gast("Cadar", "Ioana")
        gast4 = Gast("Cozma", "Denis")
        zimm1 = Zimmer(13, 2, 100, "lila", "yes")
        zimm2 = Zimmer(14, 3, 150, "yellow", "no")
        zimm3 = Zimmer(17, 4, 190, "pink", "yes")
        date_A = Zeitraum(datetime.date(2022,5,13), datetime.date(2022,6,7))
        date_B = Zeitraum(datetime.date(2020,6,8), datetime.date(2021,11,11))
        date_C = Zeitraum(datetime.date(2021,11,30), datetime.date(2021,12,15))
        res1 = Reservierung([gast1,gast2],zimm2,date_A)
        res2 = Reservierung([gast3],zimm3,date_B)
        res3 = Reservierung([gast1, gast4],zimm2,date_C)
        hotel1 = Hotel([gast1,gast2,gast3,gast4], [zimm1,zimm2,zimm3], [res1,res2,res3])
        tag = datetime.date(2021,12,1)
        assert hotel1.aktuelle_reservierung(tag) == [gast1,gast2,gast4]

def test_filter():
        zimm1 = Zimmer(13, 2, 120, "lila", "yes")
        zimm2 = Zimmer(14, 3, 200, "yellow", "no")
        zimm3 = Zimmer(17, 2, 200, "pink", "yes")
        zimm4 = Zimmer(17, 4, 300, "pink", "yes")
        zimm5 = Zimmer(17, 1, 40, "pink", "yes")
        hotel1 = Hotel([], [zimm1, zimm2, zimm3, zimm4, zimm5], [])
        assert hotel1.filter(50, 280, "yes") == [zimm1, zimm3]

def test_hinfugen_res():
        gast1 = Gast("Lucescu", "Mirela")
        gast2 = Gast("Cadar", "Ioana")
        zimm = Zimmer(13, 2, 120, "lila", "yes")
        hotel1 = Hotel([gast1, gast2], [zimm], [])
        zeit = Zeitraum((11,4,2022),(18,4,2022))
        res1 = Reservierung([gast1,gast2], zimm, zeit)
        hotel1.hinfugen_res(res1)
        assert hotel1.res_list == [res1]

def test_suchen():
        gast1 = Gast("Lucescu", "Mirela")
        gast2 = Gast("Cadar", "Ioana")
        gast3 = Gast("Sandru", "Gabriel")
        gast4 = Gast("Criste", "Cosmin")
        gast5 = Gast("Aliev", "Denis")
        zimm1 = Zimmer(13, 2, 120, "lila", "yes")
        zimm2 = Zimmer(14, 3, 200, "yellow", "no")
        zimm3 = Zimmer(17, 2, 200, "pink", "yes")
        zimm4 = Zimmer(19, 1, 400, "green", "yes")
        zimm5 = Zimmer(20, 6, 800, "violet", "no")
        zeit1 = Zeitraum(datetime.date(2022,4,11), datetime.date(2022,4,18))
        zeit2 = Zeitraum(datetime.date(2022,5,12), datetime.date(2022,5,20))
        zeit3 = Zeitraum(datetime.date(2022,4,15), datetime.date(2022,4,29))
        res1 = Reservierung([gast1, gast2], zimm2, zeit1)
        res2 = Reservierung([gast3], zimm1, zeit2)
        res3 = Reservierung([gast4,gast5], zimm3, zeit3)
        date_ankunft = datetime.date(2022,4,16)
        date_abfahrt = datetime.date(2022,4,17)
        date = Zeitraum(date_ankunft,date_abfahrt)
        nr = 2
        hotel1 = Hotel([gast1, gast2,gast3,gast4,gast5], [zimm1,zimm2,zimm3,zimm4,zimm5], [res1,res2,res3])
        assert hotel1.suchen(date,nr) == [zimm5,zimm1]

def test_frei_zimmern():
        gast1 = Gast("Sandru", "Gabriel")
        gast2 = Gast("Criste", "Cosmin")
        gast3 = Gast("Cadar", "Ioana")
        gast4 = Gast("Cozma", "Denis")
        zimm1 = Zimmer(13, 2, 100, "lila", "yes")
        zimm2 = Zimmer(14, 3, 150, "yellow", "no")
        zimm3 = Zimmer(17, 4, 190, "pink", "yes")
        date_A = Zeitraum(datetime.date(2022, 5, 13), datetime.date(2022, 6, 7))
        date_B = Zeitraum(datetime.date(2020, 6, 8), datetime.date(2021, 11, 11))
        date_C = Zeitraum(datetime.date(2021, 11, 30), datetime.date(2021, 12, 15))
        res1 = Reservierung([gast1, gast2], zimm2, date_A)
        res2 = Reservierung([gast3], zimm3, date_B)
        res3 = Reservierung([gast1, gast4], zimm2, date_C)
        hotel1 = Hotel([gast1, gast2, gast3, gast4], [zimm1, zimm2, zimm3], [res1, res2, res3])
        tag = datetime.date(2021, 12, 1)
        assert hotel1.frei_zimmern(tag) == [zimm1, zimm3]