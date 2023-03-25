from Gaste import Gast
from Reservierung import Reservierung, Zeitraum
from Gemeinsame_funktionalitat import Hotel
from Zimmern import Zimmer
import csv, datetime
def auslesen(filename):
    f = open(filename, 'r')
    csv_reader = csv.reader(f)
    gaste_list = []
    i = 0
    for line in csv_reader:
        if line[0] == '*gaste_ende':
            break
        gast = Gast(line[0], line[1])
        gaste_list.append(gast)

    zimmer_list = []
    for line in csv_reader:
        if line[0] == '*zimmer_ende':
            break
        zimm = Zimmer(int(line[0]), int(line[1]), int(line[2]), line[3], line[4])
        zimmer_list.append(zimm)

    reservierung_list = []
    gaste_l = []
    for line in csv_reader:
        if line[0] == 'g':
            gast = Gast(line[1], line[2])
            gaste_l.append(gast)
        elif line[0] == 'z':
            zimm = Zimmer(int(line[1]), int(line[2]), int(line[3]), line[4], line[5])
        elif line[0] == 'd':
            ankunft = datetime.date(int(line[1]), int(line[2]), int(line[3]))
            abfahrt = datetime.date(int(line[4]), int(line[5]), int(line[6]))
            reservierung_list.append(Reservierung(gaste_l, zimm, Zeitraum(ankunft, abfahrt)))
            gaste_l = []
        elif line[0] == '*res_e':
            gaste_l = []
        elif line[0] == '*reservierung_ende':
            break
    f.close()
    return Hotel(gaste_list, zimmer_list, reservierung_list)

def speichern(filename, hotel):
    f = open(filename, 'w', newline='')
    csv_writer = csv.writer(f)
    i = 0
    while i < len(hotel.gaste_list):
        csv_writer.writerow([hotel.gaste_list[i].nachname, hotel.gaste_list[i].vorname])
        i += 1
    csv_writer.writerow(['*gaste_ende'])

    i = 0
    while i < len(hotel.zimmer_list):
        csv_writer.writerow(
            [hotel.zimmer_list[i].nummer, hotel.zimmer_list[i].nr_gasten, hotel.zimmer_list[i].preis,
             hotel.zimmer_list[i].farbe, hotel.zimmer_list[i].meerblick])
        i += 1

    csv_writer.writerow(['*zimmer_ende'])
    i = 0
    while i < len(hotel.res_list):
        for gast in hotel.res_list[i].gaste_l:
            gaste = ['g', gast.nachname, gast.vorname]
            csv_writer.writerow(gaste)
        csv_writer.writerow(
            ['z', hotel.res_list[i].zimmer.nummer, hotel.res_list[i].zimmer.nr_gasten, hotel.res_list[i].zimmer.preis,
             hotel.res_list[i].zimmer.farbe, hotel.res_list[i].zimmer.meerblick])
        csv_writer.writerow(
            ['d', hotel.res_list[i].zeitraum.zeit_ankunft.year, hotel.res_list[i].zeitraum.zeit_ankunft.month,
             hotel.res_list[i].zeitraum.zeit_ankunft.day, hotel.res_list[i].zeitraum.zeit_abfahrt.year,
             hotel.res_list[i].zeitraum.zeit_abfahrt.month,
             hotel.res_list[i].zeitraum.zeit_abfahrt.day])
        i += 1
        csv_writer.writerow(['*res_e'])
    csv_writer.writerow(['*reservierung_ende'])
    f.close()