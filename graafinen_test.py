from tkinter import *

window = Tk()
window.title("Polttoleikkeet")
window.geometry("1060x480")

global kplk_paino
global kplhinta
global kokhinta
global omak_laske
global omak_total


def int_check1():
    try:
        int(paksuus_arvo.get())
        paksuus_arvo.config(bg="white")
    except ValueError:
        paksuus_arvo.config(bg="firebrick2")
        # Testaa onko arvot numeroita


def int_check2():
    try:
        int(leveys_arvo.get())
        leveys_arvo.config(bg="white")
    except ValueError:
        leveys_arvo.config(bg="firebrick2")
        # Testaa onko arvot numeroita


def int_check3():
    try:
        int(pituus_arvo.get())
        pituus_arvo.config(bg="white")
    except ValueError:
        pituus_arvo.config(bg="firebrick2")
        # Testaa onko arvot numeroita


def int_check4():
    try:
        int(kpl_arvo.get())
        kpl_arvo.config(bg="white")
    except ValueError:
        kpl_arvo.config(bg="firebrick2")
        # Testaa onko arvot numeroita


def int_check5():
    if kilohinta_arvo.get() == "":
        kilohinta_arvo.config(bg="firebrick2")
    else:
        kilohinta_arvo.config(bg="white")
        # Testaa onko arvokenttä tyhjä


def int_check6():
    if omak_arvo.get() == "":
        omak_arvo.config(bg="firebrick2")
    else:
        omak_arvo.config(bg="white")
        # Testaa onko arvokenttä tyhjä


def laske():
    int_check1()
    int_check2()
    int_check3()
    int_check4()
    int_check5()
    int_check6()
    if len(paksuus_arvo.get()) <= 0 or len(leveys_arvo.get()) <= 0 or len(pituus_arvo.get()) <= 0 or \
            len(kpl_arvo.get()) <= 0 or len(kilohinta_arvo.get()) <= 0 or len(omak_arvo.get()) <= 0:
        paksuus_arvo.focus_set()
        # Tarkistaa onko arvokentissä arvot
    else:
        paksuus_laske = int(paksuus_arvo.get())
        leveys_laske = int(leveys_arvo.get())
        pituus_laske = int(pituus_arvo.get())
        kpl_laske = int(kpl_arvo.get())
        kilohinta_laske = kilohinta_arvo.get()
        kilohinta_laske = kilohinta_laske.replace(",", ".")
        # Korvaa pisteen pilkulla
        try:
            kilohinta_laske = float(kilohinta_laske)
            kilohinta_arvo.config(bg="white")
        except ValueError:
            kilohinta_arvo.config(bg="firebrick2")
            # Testaa onko syöte numero/float

        kpl_paino = (paksuus_laske * leveys_laske * pituus_laske / 1000000 * 8)
        # Laskee kappalepainon

        global kplk_paino
        kplk_paino = (round(kpl_paino, 2) * kpl_laske)
        # Laskee kappaleiden kokonaispainon

        global kplhinta
        kplhinta = (paksuus_laske * leveys_laske * pituus_laske / 1000000 * 8 * kilohinta_laske)
        # Laskee kappalehinnan

        global kokhinta
        kokhinta = (round(kplhinta, 2) * kpl_laske)
        # Laskee kappaleiden kokonaishinnan

        global leikkausmetrit
        # Laskee kappaleiden leikkausmetrit

        if var1.get() == 1:
            leikkausmetrit = (((leveys_laske * 2) + (pituus_laske * 2)) / 1000 * kpl_laske / 2)
            leikkausmetrit = round(leikkausmetrit, 2)
            # Kahden viivan leikkaus päällä
        elif var1.get() == 0:
            leikkausmetrit = (((leveys_laske * 2) + (pituus_laske * 2)) / 1000 * kpl_laske)
            leikkausmetrit = round(leikkausmetrit, 2)
            # Ei kahden viivan leikkausta

        global omak_laske
        omak_laske = omak_arvo.get()
        omak_laske = omak_laske.replace(",", ".")
        try:
            omak_laske = float(omak_laske)
            omak_arvo.config(bg="white")
        except ValueError:
            omak_arvo.config(bg="firebrick2")
            # Testaa onko syöte numero/float

        omak_laske = (round(kpl_paino, 2) * omak_laske * kpl_laske)
        # Laskee kappaleiden omakustannuksen

        global leikkauskust
        global omak_total

        if var2.get() == 0:
            Chkbox.config(state="normal")
            Chkbox2.config(selectcolor="green2")
            leikkustLabel.config(fg="black")

            if paksuus_laske <= 10:
                leikkauskust = 3.04
            elif paksuus_laske <= 20:
                leikkauskust = 4.2
            elif paksuus_laske <= 30:
                leikkauskust = 5.21
            elif paksuus_laske <= 50:
                leikkauskust = 6.56
            elif paksuus_laske <= 80:
                leikkauskust = 10.09
            elif paksuus_laske <= 120:
                leikkauskust = 13.46
            elif paksuus_laske <= 250:
                leikkauskust = 25.56
            # Leikkauksen asetetut omakustannukset levypaksuuttain

            omak_total = omak_laske + leikkauskust * leikkausmetrit
            # Laskee kokonaisomakustannuksen

            kgLabel['text'] = f"{round(kpl_paino, 2)}kg"
            kplkLabel['text'] = f"{(round(kplk_paino, 2))}kg"
            kplhintaLabel['text'] = f"{round(kplhinta, 2)}€"
            kokhintaLabel['text'] = f"{round(kokhinta, 2)}€"
            leikkausmetritLabel['text'] = f"{round(leikkausmetrit, 2)}m"

            if var1.get() == 1:
                Chkbox.config(selectcolor="red")
                leikkausmetritLabel['text'] = f"{round(leikkausmetrit, 2)}m"
                leikkausmetritLabel.config(fg="red")
                # Asettaa 'leikkausmetrit' tekstin punaiseksi jos 2-viivan poltto päällä
            else:
                Chkbox.config(selectcolor="white")
                leikkausmetritLabel['text'] = f"{round(leikkausmetrit, 2)}m"
                leikkausmetritLabel.config(fg="black")
                # Asettaa 'leikkausmetrit' tekstin mustaksi jos 2-viivan poltto ei ole päällä

            leikkustLabel['text'] = f"{round(leikkauskust, 2)}" + "€/m x " + f"{round(leikkausmetrit, 2)}" + "m = " + \
                                    f"{round(leikkausmetrit * leikkauskust, 2)}" + "€"
            omakLabel['text'] = f"{round(omak_laske, 2)}€"
            # Leikkauskustannus ja omakustannus rivit

            if kokhinta - omak_total < 0:
                tkkLabel['text'] = f"{round(kokhinta, 2)}€ - " + f"{round(omak_total, 2)}€ = " + \
                                   f"{round(kokhinta - omak_total, 2)}€  " + \
                                   f"{round((1 - (omak_total / kokhinta)) * 100, 2)}%"
                tkkLabel.config(fg="red")
                # Jos kateprosentti negatiivinen, tuotto/kustannus/kate tekstin väri punainen
            else:
                tkkLabel['text'] = f"{round(kokhinta, 2)}€ - " + f"{round(omak_total, 2)}€ = " + \
                                   f"{round(kokhinta - omak_total, 2)}€  " + \
                                   f"{round((1 - (omak_total / kokhinta)) * 100, 2)}%"
                tkkLabel.config(fg="green")
                # Jos kateprosentti positiivinen, tuotto/kustannus/kate tekstin väri vihreä
        else:
            kgLabel['text'] = f"{round(kpl_paino, 2)}kg"
            kplkLabel['text'] = f"{(round(kplk_paino, 2))}kg"
            kplhintaLabel['text'] = f"{round(kplhinta, 2)}€"
            kokhintaLabel['text'] = f"{round(kokhinta, 2)}€"
            leikkausmetritLabel['text'] = f"-"
            omakLabel['text'] = f"{round(omak_laske, 2)}€"
            leikkustLabel['text'] = "0€"
            leikkustLabel.config(fg="red")
            Chkbox.config(state="disabled")
            Chkbox2.config(selectcolor="red")
            if kokhinta - omak_laske < 0:
                tkkLabel['text'] = f"{round(kokhinta, 2)}€ - " + f"{round(omak_laske, 2)}€ = " + \
                                   f"{round(kokhinta - omak_laske, 2)}€  " + \
                                   f"{round((1 - (omak_laske / kokhinta)) * 100, 2)}%"
                tkkLabel.config(fg="red")
                # Jos kateprosentti negatiivinen, tuotto/kustannus/kate tekstin väri punainen
            else:
                tkkLabel['text'] = f"{round(kokhinta, 2)}€ - " + f"{round(omak_laske, 2)}€ = " + \
                                   f"{round(kokhinta - omak_laske, 2)}€  " + \
                                   f"{round((1 - (omak_laske / kokhinta)) * 100, 2)}%"
                tkkLabel.config(fg="green")
            # Jos kateprosentti positiivinen, tuotto/kustannus/kate tekstin väri vihreä

        paksuus_arvo.config(state="disabled")
        leveys_arvo.config(state="disabled")
        pituus_arvo.config(state="disabled")
        kpl_arvo.config(state="disabled")
        kilohinta_arvo.config(state="disabled")
        omak_arvo.config(state="disabled")
        # Asettaa tekstikentät disable tilaan
        btn_siirra["state"] = "normal"
        btn_siirra["bg"] = "green"
        # Siirrä nappi aktiiviseksi
        Chkbox.config(state="disabled")
        Chkbox2.config(state="disabled")
        # Disabloi checkboxit


def empty():
    paksuus_arvo.config(state="normal")
    leveys_arvo.config(state="normal")
    pituus_arvo.config(state="normal")
    kpl_arvo.config(state="normal")
    kilohinta_arvo.config(state="normal")
    omak_arvo.config(state="normal")
    # Asettaa tekstikentät normaaliksi
    paksuus_arvo.config(bg="white")
    leveys_arvo.config(bg="white")
    pituus_arvo.config(bg="white")
    kpl_arvo.config(bg="white")
    kilohinta_arvo.config(bg="white")
    omak_arvo.config(bg="white")
    # Asettaa tekstikentän värin valkoiseksi
    paksuus_arvo.delete(0, END)
    leveys_arvo.delete(0, END)
    pituus_arvo.delete(0, END)
    kpl_arvo.delete(0, END)
    kilohinta_arvo.delete(0, END)
    omak_arvo.delete(0, END)
    kgLabel.config(text="")
    kplkLabel.config(text="")
    kplhintaLabel.config(text="")
    kokhintaLabel.config(text="")
    leikkausmetritLabel.config(text="")
    leikkustLabel.config(text="")
    omakLabel.config(text="")
    tkkLabel.config(text="")
    paksuus_arvo.focus_set()
    # Tyhjentää kentät, 'paksuus_arvo.focus_set()' asettaa kursorin 'Paksuus' kenttään
    btn_siirra["state"] = "disabled"
    btn_siirra["bg"] = "gray81"
    # Siirrä näppi ei aktiiviseksi
    Chkbox.config(state="normal")
    Chkbox2.config(state="normal")
    # Aktivoi checkboxit


def siirra():
    if len(paksuus_arvo.get()) <= 0 or len(leveys_arvo.get()) <= 0 or len(pituus_arvo.get()) <= 0 or \
            len(kpl_arvo.get()) <= 0 or len(kilohinta_arvo.get()) <= 0 or len(omak_arvo.get()) <= 0:
        paksuus_arvo.focus_set()
        # Tarkistaa onko arvokentissä arvot
    else:
        listbox.insert(listbox.size(), "TL " + paksuus_arvo.get() + "x" + leveys_arvo.get() +
                       "x" + pituus_arvo.get() + "mm  " + kpl_arvo.get() + "kpl  " + str(round(kplhinta, 2)) + "€/kpl")
        listbox2.insert(listbox.size(), round(kokhinta, 2))
        listbox3.insert(listbox.size(), round(kplk_paino, 2))
        listbox4.insert(listbox.size(), leikkausmetrit)
        if var2.get() == 0:
            listbox5.insert(listbox.size(), round(omak_total, 2))
            listbox6.insert(listbox.size(), round(kokhinta - omak_total, 2))
            listbox7.insert(listbox.size(), round((1 - (omak_total / kokhinta)) * 100, 2))
        else:
            listbox5.insert(listbox.size(), round(omak_laske, 2))
            listbox6.insert(listbox.size(), round(kokhinta - omak_laske, 2))
            listbox7.insert(listbox.size(), round((1 - (omak_laske / kokhinta)) * 100, 2))
            # Jos leikkauskustannuksia ei lasketa
        paksuus_arvo.focus_set()
        sum_values()
        sum_valueskg()
        sum_valuesm()
        sum_valueok()
        sum_valueprof()
        sum_valuewin()
        # Siirtää lasketut arvot listboxeihin, 'paksuus_arvo.focus_set()' asettaa kursorin 'Paksuus' kenttään,
        # tyhjentää arvokentät ja laskee listboxien kokonaisarvot
        paksuus_arvo.config(state="normal")
        leveys_arvo.config(state="normal")
        pituus_arvo.config(state="normal")
        kpl_arvo.config(state="normal")
        kilohinta_arvo.config(state="normal")
        omak_arvo.config(state="normal")
        # Asettaa tekstikentät normaaleiksi
        empty()
        btn_siirra["state"] = "disabled"
        btn_siirra["bg"] = "gray81"
        # Siirrä näppi ei aktiiviseksi
        Chkbox.config(state="normal")
        Chkbox2.config(state="normal")
        # Aktivoi checkboxit


def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
        listbox2.delete(i)
        listbox3.delete(i)
        listbox4.delete(i)
        listbox5.delete(i)
        listbox6.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox2.curselection()):
        listbox2.delete(i)
        listbox.delete(i)
        listbox3.delete(i)
        listbox4.delete(i)
        listbox5.delete(i)
        listbox6.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox3.curselection()):
        listbox3.delete(i)
        listbox4.delete(i)
        listbox.delete(i)
        listbox2.delete(i)
        listbox5.delete(i)
        listbox6.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox4.curselection()):
        listbox4.delete(i)
        listbox.delete(i)
        listbox2.delete(i)
        listbox3.delete(i)
        listbox5.delete(i)
        listbox6.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox5.curselection()):
        listbox5.delete(i)
        listbox.delete(i)
        listbox2.delete(i)
        listbox3.delete(i)
        listbox4.delete(i)
        listbox6.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox6.curselection()):
        listbox6.delete(i)
        listbox.delete(i)
        listbox2.delete(i)
        listbox3.delete(i)
        listbox5.delete(i)
        listbox4.delete(i)
        listbox7.delete(i)
    for i in reversed(listbox7.curselection()):
        listbox7.delete(i)
        listbox.delete(i)
        listbox2.delete(i)
        listbox3.delete(i)
        listbox5.delete(i)
        listbox6.delete(i)
        listbox4.delete(i)
    sum_values()
    sum_valueskg()
    sum_valuesm()
    sum_valueok()
    sum_valueprof()
    sum_valuewin()
    paksuus_arvo.focus_set()
    # Poistaa listboxeista valitun rivin kaikki arvot, ja laskee listboxien kokonaisarvot,
    # 'paksuus_arvo.focut_set()' asettaa kursorin 'Paksuus' kenttään


def muokkaa():
    paksuus_arvo.config(state="normal")
    leveys_arvo.config(state="normal")
    pituus_arvo.config(state="normal")
    kpl_arvo.config(state="normal")
    kilohinta_arvo.config(state="normal")
    omak_arvo.config(state="normal")
    # Asettaa tekstikentät normaaleiksi
    btn_siirra["state"] = "disabled"
    btn_siirra["bg"] = "gray81"
    # Siirrä näppi ei aktiiviseksi
    Chkbox.config(state="normal")
    Chkbox2.config(state="normal")
    # Aktivoi checkboxit


def sum_values():
    totalee = sum(listbox2.get(0, END))
    sum_valuee.set(totalee)
    totaleeLabel['text'] = f"{round(totalee, 2)}€"
    # Laskee listboxien kokonaiseurot


def sum_valueskg():
    total = sum(listbox3.get(0, END))
    sum_value.set(total)
    totalLabel['text'] = f"{round(total, 2)}kg"
    # Laskee listboxien kokonaiskilot


def sum_valuesm():
    totalm = sum(listbox4.get(0, END))
    sum_valuem.set(totalm)
    totalmLabel['text'] = f"{round(totalm, 2)}m"
    # Laskee listboxien kokonaisleikkausmetrit


def sum_valueok():
    totalok = sum(listbox5.get(0, END))
    sum_valueokust.set(totalok)
    totalokLabel['text'] = f"{round(totalok, 2)}€"
    # Laskee listboxien kokonaisomakustannukset


def sum_valueprof():
    if sum(listbox6.get(0, END)) < 0:
        totalt = sum(listbox6.get(0, END))
        sum_valuetuotto.set(totalt)
        totaltLabel['text'] = f"{round(totalt, 2)}€"
        totaltLabel.config(fg="red")
        # Laskee kokonaiskatteen ja muuttaa tekstin punaiseksi jos arvo negatiivinen
    elif sum(listbox6.get(0, END)) == 0:
        totalt = sum(listbox6.get(0, END))
        sum_valuetuotto.set(totalt)
        totaltLabel['text'] = f"{round(totalt, 2)}€"
        totaltLabel.config(fg="black")
        # Laskee kokonaiskatteen ja muuttaa tekstin mustaksi jos arvo 0
    else:
        totalt = sum(listbox6.get(0, END))
        sum_valuetuotto.set(totalt)
        totaltLabel['text'] = f"{round(totalt, 2)}€"
        totaltLabel.config(fg="green")
        # Laskee kokonaiskatteen ja muuttaa tekstin vihreäksi jos arvo positiivinen


def sum_valuewin():
    if len(listbox7.get(0, END)) >= 1:
        totalwin = (1 - (sum(listbox5.get(0, END)) / sum(listbox2.get(0, END)))) * 100
        sum_valuekate.set(totalwin)
        totalwinLabel['text'] = f"{round(totalwin, 2)}%"
        # Laskee listboxien kokonaiskateprosentin
        if (1 - (sum(listbox5.get(0, END)) / sum(listbox2.get(0, END)))) * 100 < 0:
            totalwinLabel['text'] = f"{round(totalwin, 2)}%"
            totalwinLabel.config(fg="red")
            # Laskee listboxien kokonaiskateprosentin ja muuttaan tekstin punaiseksi jos arvo negatiivinen
        else:
            totalwinLabel['text'] = f"{round(totalwin, 2)}%"
            totalwinLabel.config(fg="green")
            # Muuttaa tekstin värin vihreäksi jos arvo positiivinen
    else:
        totalwin = sum(listbox7.get(0, END))
        sum_valuekate.set(totalwin)
        totalwinLabel['text'] = f"{round(totalwin, 2)}%"
        totalwinLabel.config(fg="black")
        # Jos listboxit tyhjiä, muuttaa tekstin värin mustaksi


listbox = Listbox(window, width=45, height=20, selectmode=MULTIPLE)
listbox.pack()
listbox.place(x=400, y=21)
listbox2 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox2.pack()
listbox2.place(x=670, y=21)
listbox3 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox3.pack()
listbox3.place(x=730, y=21)
listbox4 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox4.pack()
listbox4.place(x=790, y=21)
listbox5 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox5.pack()
listbox5.place(x=860, y=21)
listbox6 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox6.pack()
listbox6.place(x=920, y=21)
listbox7 = Listbox(window, width=10, height=20, selectmode=MULTIPLE)
listbox7.pack()
listbox7.place(x=980, y=21)
# Listboxien koot ja koordinaatit


paksuus = Label(window, text="Paksuus:", font="arial 10")
leveys = Label(window, text="Leveys:", font="arial 10")
pituus = Label(window, text="Pituus:", font="arial 10")
kplmaara = Label(window, text="KPL:", font="arial 10")
kilohinta = Label(window, text="Kilohinta €/kg:", font="arial 10")
kappalepaino = Label(window, text="Kappalepaino:", font="arial 10")
kokonaispaino = Label(window, text="Kokonaispaino:", font="arial 10")
kappalehinta = Label(window, text="Kappalehinta:", font="arial 10")
kokonaishinta = Label(window, text="Kokonaishinta:", font="arial 10")
leikkausmetrit = Label(window, text="Leikkausmetrit:", font="arial 10")
leikkauskust = Label(window, text="Leikkauskustannukset:", font="arial 10")
omak = Label(window, text="Omakustannus €/kg:", font="arial 10")
omak_label = Label(window, text="Levyn omakustannus:", font="arial 10")
tulos = Label(window, text="Tuotto/Kustannus/Kate:", font="arial 10")
kg = Label(window, text="KG yht:", font="arial 10")
totaleuro = Label(window, text="€ yht:", font="arial 10")
leikm = Label(window, text="Leik. M:", font="arial 10")
kgyla = Label(window, text="KG:", font="arial 9")
totaleuroyla = Label(window, text="€:", font="arial 9")
leikmyla = Label(window, text="Leik. M:", font="arial 9")
omakyla = Label(window, text="Omak.", font="arial 9")
tuotto = Label(window, text="Tuotto", font="arial 9")
kate = Label(window, text="Kate %", font="arial 9")
omakala = Label(window, text="Omak.:", font="arial 9")
tuottoala = Label(window, text="Tuotto:", font="arial 9")
kateala = Label(window, text="Kate %:", font="arial 9")
# Tekstit

kgLabel = Label(window, font="arial 10 bold")
kgLabel.place(x=200, y=205)
kplkLabel = Label(window, font="arial 10 bold")
kplkLabel.place(x=200, y=235)
kplhintaLabel = Label(window, font="arial 10 bold")
kplhintaLabel.place(x=200, y=265)
kokhintaLabel = Label(window, font="arial 10 bold")
kokhintaLabel.place(x=200, y=295)
leikkausmetritLabel = Label(window, font="arial 10 bold")
leikkausmetritLabel.place(x=200, y=325)
leikkustLabel = Label(window, font="arial 10 bold")
leikkustLabel.place(x=200, y=355)
omakLabel = Label(window, font="arial 10 bold")
omakLabel.place(x=200, y=385)
tkkLabel = Label(window, font="arial 10 bold")
tkkLabel.place(x=200, y=415)
totaleeLabel = Label(window, text="0€", font="arial 10 bold")
totaleeLabel.place(x=730, y=365)
totalLabel = Label(window, text="0kg", font="arial 10 bold")
totalLabel.place(x=730, y=385)
totalmLabel = Label(window, text="0m", font="arial 10 bold")
totalmLabel.place(x=730, y=405)
totalokLabel = Label(window, text="0€", font="arial 10 bold")
totalokLabel.place(x=920, y=365)
totaltLabel = Label(window, text="0€", font="arial 10 bold")
totaltLabel.place(x=920, y=385)
totalwinLabel = Label(window, text="0%", font="arial 10 bold")
totalwinLabel.place(x=920, y=405)
# Tekstien fontit ja koordinaatit

paksuus.place(x=50, y=25)
leveys.place(x=50, y=55)
pituus.place(x=50, y=85)
kplmaara.place(x=50, y=115)
kilohinta.place(x=50, y=145)
omak.place(x=50, y=175)
kappalepaino.place(x=50, y=205)
kokonaispaino.place(x=50, y=235)
kappalehinta.place(x=50, y=265)
kokonaishinta.place(x=50, y=295)
leikkausmetrit.place(x=50, y=325)
leikkauskust.place(x=50, y=355)
omak_label.place(x=50, y=385)
tulos.place(x=50, y=415)
totaleuro.place(x=670, y=365)
kg.place(x=670, y=385)
leikm.place(x=670, y=405)
totaleuroyla.place(x=670, y=0)
kgyla.place(x=730, y=0)
leikmyla.place(x=790, y=0)
omakyla.place(x=860, y=0)
tuotto.place(x=920, y=0)
kate.place(x=980, y=0)
omakala.place(x=860, y=365)
tuottoala.place(x=860, y=385)
kateala.place(x=860, y=405)
# Arvokenttien koordinaatit

paksuus_arvo = StringVar()
leveys_arvo = StringVar()
pituus_arvo = StringVar()
kpl_arvo = StringVar()
kilohinta_arvo = StringVar()
omak_arvo = StringVar()
sum_value = StringVar()
sum_valuee = StringVar()
sum_valuem = StringVar()
sum_valueokust = StringVar()
sum_valuetuotto = StringVar()
sum_valuekate = StringVar()
var1 = IntVar()
var2 = IntVar()

paksuus_arvo = Entry(window, textvariable=paksuus_arvo, font="arial 10", width=15)
paksuus_arvo.place(x=200, y=25)
leveys_arvo = Entry(window, textvariable=leveys_arvo, font="arial 10", width=15)
leveys_arvo.place(x=200, y=55)
pituus_arvo = Entry(window, textvariable=pituus_arvo, font="arial 10", width=15)
pituus_arvo.place(x=200, y=85)
kpl_arvo = Entry(window, textvariable=kpl_arvo, font="arial 10", width=15)
kpl_arvo.place(x=200, y=115)
kilohinta_arvo = Entry(window, textvariable=kilohinta_arvo, font="arial 10", width=15)
kilohinta_arvo.place(x=200, y=145)
omak_arvo = Entry(window, textvariable=omak_arvo, font="arial 10", width=15)
omak_arvo.place(x=200, y=175)
# Kirjoituskenttien fontit ja koordinaatit

btn_laske = Button(window, text="Laske", font="arial 12", bg="white", bd=3, command=laske)
btn_laske.pack()
btn_laske.place(x=50, y=440)
btn_empty = Button(window, text="Tyhjennä", font="arial 12", bg="white", bd=3, command=empty)
btn_empty.pack()
btn_empty.place(x=150, y=440)
btn_siirra = Button(window, text="Siirrä", font="arial 12", bg="gray81", bd=3, command=siirra, state="disabled")
btn_siirra.pack()
btn_siirra.place(x=300, y=440)
btn_delete = Button(window, text="Poista", font="arial 12", bg="white", bd=3, command=delete)
btn_delete.pack()
btn_delete.place(x=400, y=440)
btn_muokkaa = Button(window, text="Muokkaa", font="arial 12", bg="white", bd=3, command=muokkaa)
btn_muokkaa.pack()
btn_muokkaa.place(x=315, y=160)
# Painikkeiden nimet, fontit, värit, komennot ja koordinaatit

Chkbox = Checkbutton(window, text="2-viivan", font="arial 10", onvalue=1, offvalue=0, variable=var1)
Chkbox.place(x=300, y=323)
# 2-viivan polton checkbox

Chkbox2 = Checkbutton(window, font="arial 10", onvalue=0, offvalue=1, variable=var2, selectcolor="green2")
Chkbox2.place(x=20, y=353)

window.bind('<Return>', lambda event: laske())
window.bind('<Shift_L>' + '<Return>', lambda event: siirra())
window.bind('<Delete>', lambda event: delete())
# Näppäimistön pikanäppäimet

window.mainloop()
