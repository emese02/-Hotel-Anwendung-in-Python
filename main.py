from Gemeinsame_funktionalitat import Hotel, zeige_list
from Gaste import Gast
from Reservierung import Reservierung, Zeitraum
from Zimmern import Zimmer
import datetime
from auslesen_und_speicher import auslesen, speichern
from Teste import *


def menu_gaste():
    return """
    Option 1: Add guest
    Option 2: Modify last name
    Option 3: Delete a guest
    Option 4: Show list of guests
    Option 5: Back to main menu
    """


def menu_zimmern():
    return """
    Option 1: Add new room
    Option 2: Actualize the price of a room
    Option 3: Delete a room
    Option 4: Show list of rooms
    Option 5: Back to main menu
    """


def menu_gemeinsam():
    return """
    Option 1: Make a reservation
    Option 2: Show guests with actual reservations
    Option 3: Filter room (by price and sea-view critery)
    Option 4: Show free rooms today
    Option 5: Back to main menu
    """


def menu():
    return """
    Option 1: Guest menu
    Option 2: Room menu
    Option 3: Together menu    
    Option 4: Save all changes
    """


def main():
    hotel = auslesen('datei.txt')
    while True:
        print(menu())
        option = int(input("Choose an option: "))

        if option == 1:
            opt = 0
            while opt != 5:
                print(menu_gaste())
                opt = int(input("Choose an option: "))
                if opt == 1:
                    nachname = input("Last name: ")
                    vorname = input("First name: ")
                    hotel.hinfugen_gast(Gast(nachname, vorname))
                    print("We registered the guest.")
                    test_hinfugen_gast()

                elif opt == 2:
                    nachname = input("Last name: ")
                    vorname = input("First name: ")
                    gast_index = hotel.identifizieren_gast(nachname,vorname)
                    if gast_index is None:
                        print("The guest is not registered.")
                    else:
                        gast_neu_name = input("The new last name: ")
                        hotel.update_gast(gast_index, gast_neu_name)
                        print("The name was updated.")
                        test_aktualisierung_nachname()
                        test_update_gast()
                    test_identifizieren_gast()

                elif opt == 3:
                    nachname = input("Last name: ")
                    vorname = input("First name: ")
                    gast_index = hotel.identifizieren_gast(nachname, vorname)
                    if gast_index is not None:
                        hotel.loschen_gast(gast_index)
                        print("We deleted the guest.")
                    else:
                        print("We don't have a registered guest with the given name.")
                    test_loschen_gast()
                    test_identifizieren_gast()

                elif opt == 4:
                    hotel.zeigen_listen("gaste")

                elif opt!= 5:
                    print("The asked option doesn't exist.")

        elif option == 2:
            opt = 0
            while opt != 5:
                print(menu_zimmern())
                opt = int(input("Choose an option: "))

                if opt == 1:
                    nr = int(input("Room nr: "))
                    zimmer_index = hotel.identifizieren_zimmer(nr)
                    if zimmer_index is not None:
                        print("We already have a room with the given number.")
                    else:
                        nr_gaste = int(input("Number of guests: "))
                        preis = int(input("Price: "))
                        farbe = input("Color: ")
                        meerblick = input("Sea-view (yes/no): ")
                        hotel.hinfugen_Zimmer(Zimmer(nr, nr_gaste, preis, farbe, meerblick))
                        print("We added the room.")
                    test_hinfugen_zimmer()
                    test_identifizierien_zimmer()

                elif opt == 2:
                    nr = int(input("Room nr: "))
                    zimmer_index = hotel.identifizieren_zimmer(nr)
                    if zimmer_index is not None:
                        neue_preis = int(input("New price: "))
                        hotel.update_zimmer(zimmer_index, neue_preis)
                        print("The price was updated.")
                    else:
                        print("We don't have a room with the given number.")
                    test_identifizierien_zimmer()
                    test_aktualisieren_preis()
                    test_update_zimmer()

                elif opt == 3:
                    nr = int(input("Number of the room that should be deleted: "))
                    zimmer_index = hotel.identifizieren_zimmer(nr)
                    if zimmer_index is not None:
                        hotel.loschen_zimmer(zimmer_index)
                        print("The room was deleted.")
                    else:
                        print("We don't have a room with the given number.")
                    test_identifizierien_zimmer()
                    test_loschen_zimmer()

                elif opt == 4:
                    hotel.zeigen_listen("zimmer")
                elif opt != 5:
                    print("The asked option doesn't exist.")

        elif option == 3:
            opt = 0
            while opt != 5:
                print(menu_gemeinsam())
                opt = int(input("Choose an option: "))
                if opt == 1:
                    print("-Arrival-")
                    jahr_ankunft = int(input("Year of arrival: "))
                    monat_ankunft = int(input("Month of arrival: "))
                    tag_ankunft = int(input("Day of arrival: "))
                    ankunft = datetime.date(jahr_ankunft, monat_ankunft, tag_ankunft)
                    if ankunft < datetime.date.today():
                        print("Unfortunately, you can't make a reservation in the past.")
                    else:
                        print("-Departure-")
                        jahr_abfahrt = int(input("Year of departure: "))
                        monat_abfahrt = int(input("Month of departure: "))
                        tag_abfahrt = int(input("Day of departure: "))
                        abfahrt = datetime.date(jahr_abfahrt,monat_abfahrt,tag_abfahrt)
                        zeit = Zeitraum(ankunft,abfahrt)
                        nr = int(input("Number of arriving guests: "))
                        list_moglichkeit = hotel.suchen(zeit, nr)
                        if len(list_moglichkeit) > 0:
                            print("Possible choices: ")
                            zeige_list(list_moglichkeit)
                            option = int(input("Write here the number of the chosen room: "))
                            res_gaste = []             #wir bilden eine Liste von den Gasten, die wollen reservieren
                            while nr > 0:
                                gast_vorname = input("First name of the guest: ")
                                gast_nachname = input("Last name of the guest: ")
                                gast_index = hotel.identifizieren_gast(gast_nachname,gast_vorname)
                                if gast_index is not None:
                                    res_gaste.append(hotel.gaste_list[gast_index])
                                else:
                                    gast = Gast(gast_nachname, gast_vorname)
                                    res_gaste.append(gast)
                                nr -= 1
                            index = hotel.identifizieren_zimmer(option)
                            zimm = hotel.zimmer_list[index]
                            reservier = Reservierung(res_gaste, zimm, zeit)
                            hotel.hinfugen_res(reservier)
                            print("The reservation was succesful.")
                            i = 0
                            while i < len(res_gaste):
                                gast_index = hotel.identifizieren_gast(gast_nachname, gast_vorname)
                                if gast_index is None:
                                    hotel.hinfugen_gast(res_gaste[i])
                                    test_hinfugen_gast()
                                i += 1
                        else:
                            print("Unfortunately we don't have any free rooms for", nr, " people")
                        test_hinfugen_res()
                        test_identifizieren_gast()
                        test_kein_durchschnitt()
                        test_suchen()

                elif opt == 2:
                    zeige_list(hotel.aktuelle_reservierung(datetime.date.today()))
                    test_aktuelle_reservierung()

                elif opt == 3:
                    meerblick = input("Do you want sea-view? (yes/no): ")
                    maximal = int(input("Maximal price: "))
                    minimal = int(input("Minimal price: "))
                    if len(hotel.filter(minimal,maximal,meerblick))>0:
                        zeige_list(hotel.filter(minimal, maximal, meerblick))
                    else:
                        print("Our hotel doesn't have rooms with the given criteria.")
                    test_filter()

                elif opt == 4:
                    frei_zimm = hotel.frei_zimmern(datetime.date.today())
                    if len(frei_zimm) > 0:
                        zeige_list(hotel.frei_zimmern(datetime.date.today()))
                    else:
                        print("We don't have free rooms.")
                    test_frei_zimmern()
                elif opt!=5:
                    print("The asked option doesn't exist.")

        elif option == 4:
                speichern("datei.txt",hotel)
                print("We saved the changes.")
        else:
            print("The asked option doesn't exist.")

main()
