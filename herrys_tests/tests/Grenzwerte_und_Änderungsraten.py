import datetime
import sys
import os

import pylatex, math, random, sympy, numpy, matplotlib
from random import randrange, randint, choice
from sympy import *
import matplotlib.pyplot as plt
from pylatex import Document, NoEscape, SmallText, LargeText, MediumText, NewPage, Tabular, Alignat, Figure, Center
from pylatex.utils import bold


# Definition der Funktionen
a, b, c, d, e, f, g, x, y, z = symbols('a b c d e f g x y z')
fig = plt.Figure()

path = str()


def zzahl(p, q):
    k = random.choice([-1, 1]) * random.randint(p, q)
    return k


def nzahl(p, q):
    k = random.randint(p, q)
    return k


def vorz_str(k):
    if k < 0:
        k = latex(k)
    else:
        k = '+' + latex(k)
    return k


def vorz_str_minus(k):
    if k < 0:
        k = '(' + latex(k) + ')'
    else:
        k = latex(k)
    return k


def erstellen(klasse=None, kurs=None, lehrer=None):
    def Graph(a, b, xwert, f, n, name):
        ax = plt.gca()
        ax.spines['top'].set_color('none')
        ax.spines['right'].set_color('none')
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.set_xlabel('x', size=10, labelpad=-24, x=1.03)
        ax.set_ylabel('y', size=10, labelpad=-21, y=1.02, rotation=0)
        ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)
        arrow_fmt = dict(markersize=4, color='black', clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.annotate(n, xy=(xwert, f.subs(x, xwert)), xycoords='data', xytext=(+5, +5), textcoords='offset points',
                     fontsize=12)
        plt.grid(True)
        plt.xticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.yticks(numpy.linspace(-5, 5, 11, endpoint=True))
        plt.axis([-6, 6, -6, 6])
        plt.plot(a, b, linewidth=2)
        return plt.savefig(name, dpi=200)


    # Berechnung für die Aufgaben
    def folgen(nr, teilaufg):
        liste_teilaufg = [a, b, c, d]
        i = 0
        Punkte = 0
        start_arithm_folge = zzahl(1, 10)
        start_geom_folge = nzahl(1, 10)
        arithm_folge_d = nzahl(2, 10)
        basis = zzahl(2, 10)
        if nzahl(1, 2) == 1:
            p = random.choice([2, 4, 5, 8, 10])
            geom_folge_q = Rational(1, p)
        else:
            geom_folge_q = random.choice([2, 3, 4, 5])
        bel_vorschrift = [start_arithm_folge + basis ** x,
                          start_arithm_folge - 1 / x,
                          start_arithm_folge / (x + arithm_folge_d),
                          x ** arithm_folge_d]
        bel_vorschrift_str = [str(start_arithm_folge) + r'+ \left( ' + str(basis) + r' \right) ^{n}',
                              str(start_arithm_folge) + r'~-~ \frac{1}{n}',
                              r' \frac{' + str(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                              r'n^{' + str(arithm_folge_d) + '}']
        ausw_folge = random.randint(1, len(bel_vorschrift)) - 1
        a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                    start_geom_folge * geom_folge_q ** (x - 1),
                    bel_vorschrift[ausw_folge]]
        a_n_str_alle = [latex(start_arithm_folge) + r'~+~ (n-1) \cdot ~' + latex(arithm_folge_d),
                        latex(start_geom_folge) + r' \cdot ' + latex(geom_folge_q) + r'^{n-1}',
                        bel_vorschrift_str[ausw_folge]]
        auswahl_folgenart = random.randint(1, len(a_n_alle)) - 1
        a_n = a_n_alle[auswahl_folgenart]
        a_n_str = a_n_str_alle[auswahl_folgenart]
        data = [a_n.subs(x, i) for i in range(1, 5)]
        data_lsg = [a_n.subs(x, i) for i in range(1, 8)]
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Zahlenfolge:',
                   latex(data[0]) + r', \quad ' + latex(data[1]) + r', \quad ' + latex(data[2]) + r', \quad ' +
                   latex(data[3]) + r', ~ ...  \\']
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        if a in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Setze die Zahlenfolge um drei weitere Glieder fort. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad ' + latex(data_lsg[0]) + ',~' + latex(data_lsg[1]) + ',~' +
                       latex(data_lsg[2]) + ',~' + latex(data_lsg[3]) + r',~' + latex(data_lsg[4]) + ',~' +
                       latex(data_lsg[5]) + ',~' + latex(data_lsg[6]) + r' \quad (3P)')
            Punkte += 3
            i += 1

        if b in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Überprüfe ob es sich um eine arithmetische oder geometrische '
                                                    'Zahlenfolge handelt. \n\n')
            if auswahl_folgenart == 0:
                table_b = Tabular('|c|c|c|c|', row_height=1.2)
                table_b.add_hline(1, 4)
                table_b.add_row('Differenz der Werte', 'a1-a0', 'a2-a1', 'a3-a2')
                table_b.add_hline(1, 4)
                table_b.add_row('Ergebnis', data[1] - data[0], data[2] - data[1], data[3] - data[2])
                table_b.add_hline(1, 4)
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                r'~ist~es~eine~arithmetische~Folge~mit~d~=~'
                           + str(arithm_folge_d) + r'.} \quad (3P)')
                loesung.append(table_b)
            if auswahl_folgenart == 1:
                table_b = Tabular('|c|c|c|c|', row_height=1.2)
                table_b.add_hline(1, 4)
                table_b.add_row('Quotient der Werte', 'a1/a0', 'a2/a1', 'a3/a2')
                table_b.add_hline(1, 4)
                table_b.add_row('Ergebnis', Rational(data[1], data[0]), Rational(data[2] / data[1]),
                                Rational(data[3] / data[2]))
                table_b.add_hline(1, 4)
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                r'~ist~es~eine~geometrische~Folge~mit~q~=~'
                               + str(geom_folge_q) + r'.} \quad (3P)')
                loesung.append(table_b)
            if auswahl_folgenart == 2:
                table_b = Tabular('|c|c|c|c|c|', row_height=1.2)
                table_b.add_hline(1, 5)
                table_b.add_row('Quotient der Werte', 'a1-a0', 'a2-a1', 'a1/a0', 'a2/a1')
                table_b.add_hline(1, 5)
                table_b.add_row('Ergebnis', data[1] - data[0], data[2] - data[1], N(data[1] / data[0], 3),
                                N(data[2] / data[1], 4))
                table_b.add_hline(1, 5)
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Wie~man~in~der~Tabelle~erkennen~kann,'
                                                r'~ist~weder~eine~arithmetische,~noch~eine~geometrische~Folge.} '
                                                r'\quad (3P)')
                loesung.append(table_b)
            Punkte += 3
            i += 1
        if c in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Nenne das Bildungsgesetz der Zahlenfolge. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad a_n~=~' + a_n_str + r' \quad (2P)')
            Punkte += 2
            i += 1
        if d in teilaufg and auswahl_folgenart < 2:
            if auswahl_folgenart == 0:
                a_unten = nzahl(1, 50)
                a_oben = nzahl(51, 100)
                n = a_oben - a_unten
                wert_a_unten = a_n.subs(x, a_unten)
                wert_a_oben = a_n.subs(x, a_oben)
                aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Summe der Folgenglieder von n={a_unten} bis n={a_oben}. \n\n')
                ergebnis = n * (wert_a_oben + wert_a_unten) / 2
                loesung.append(str(liste_teilaufg[i]) + r') \quad \displaystyle\sum_{i=' + str(a_unten) + '}^{' +
                                str(a_oben) + r'} ~ a_n ~=~ ' + str(n) + r' \cdot \frac{~' + str(wert_a_unten) +
                                vorz_str(wert_a_oben) + '~}{~2~} ~=~' + str(N(ergebnis, 5)) + r' \quad (3P) \\')
        else:
            a_unten = nzahl(11, 20)
            a_oben = nzahl(21, 30)
            n = a_oben - a_unten
            aufgabe.append(str(liste_teilaufg[i]) + f') Berechnen Sie die Summe der Folgenglieder von n={a_unten} bis n={a_oben}. \n\n')
            ergebnis = (1 - geom_folge_q ** (n + 1)) / (1 - geom_folge_q)
            loesung.append(str(liste_teilaufg[i]) + r') \quad \displaystyle\sum_{i=' + str(a_unten) + '}^{' +
                           str(a_oben) + r'} ~ q^n ~=~ \frac{~1~-~ \left(' + str(geom_folge_q) + r' \right)^{' + str(n + 1) +
                           '~}}{~1~-~' + str(geom_folge_q) + '} ~=~' + str(N(ergebnis, 5)) + r' \quad (3P) \\')
            Punkte += 3
            i += 1
        print(data)
        print(a_n)
        print(auswahl_folgenart)
        return [aufgabe, loesung, Punkte]


    def grenzwerte_folgen(nr, teilaufg):
        liste_teilaufg = [a, b, c, d]
        i = 0
        Punkte = 0
        start_arithm_folge = zzahl(2, 10)
        start_geom_folge = nzahl(2, 10)
        arithm_folge_d = nzahl(2, 10)
        basis = zzahl(2, 10)
        if nzahl(1, 2) == 1:
            p = random.choice([2, 4, 5, 8, 10])
            geom_folge_q = Rational(1, p)
        else:
            geom_folge_q = random.choice([2, 3, 4, 5])
        bel_vorschrift = [start_arithm_folge + basis ** x,
                          start_arithm_folge - 1 / x,
                          start_arithm_folge / (x + arithm_folge_d),
                          x ** arithm_folge_d]
        bel_vorschrift_str = [str(start_arithm_folge) + vorz_str(basis) + r'^{n}',
                              str(start_arithm_folge) + r'~-~ \frac{1}{n}',
                              r' \frac{' + str(start_arithm_folge) + r'}{n~' + vorz_str(arithm_folge_d) + '}',
                              r'n^{' + str(arithm_folge_d) + '}']
        ausw_folge = random.randint(1, len(bel_vorschrift)) - 1
        a_n_alle = [start_arithm_folge + (x - 1) * arithm_folge_d,
                    start_geom_folge * geom_folge_q ** (x - 1),
                    bel_vorschrift[ausw_folge]]
        a_n_str_alle = [latex(start_arithm_folge) + r'~+~ (n-1) \cdot ~' + latex(arithm_folge_d),
                        latex(start_geom_folge) + r' \cdot \left(' + latex(geom_folge_q) + r' \right) ^{n-1}',
                        bel_vorschrift_str[ausw_folge]]
        auswahl_folgenart = random.randint(1, len(a_n_alle)) - 1
        a_n = a_n_alle[auswahl_folgenart]
        a_n_str = a_n_str_alle[auswahl_folgenart]
        grenzwert = limit(a_n, x, oo)
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Bildungsvorschrift:',
                   r'a_{n}~=~' + a_n_str]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        if a in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Berechne den Grenzwert der gegebenen Folge. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \lim \limits_{n \to \infty } ' + a_n_str + '~=~'
                           + latex(grenzwert) + r' \quad (2P)')
            Punkte += 2
            i += 1
        return [aufgabe, loesung, Punkte]


    def grenzwerte_funktionen(nr, teilaufg):
        liste_teilaufg = [a, b, c, d]
        i = 0
        Punkte = 0
        faktor = zzahl(1, 10)
        polstelle = zzahl(1, 8)
        zaehler = expand(faktor * (x ** 2 - polstelle ** 2))
        if polstelle > 0:
            nenner = x - polstelle
            fkt_gekuerzt = r'~=~ \lim \limits_{x \to ' + str(polstelle) + '} ~ ' + latex(faktor) + \
                           r' \cdot (x~' + vorz_str(-1 * polstelle) + '~)'
        else:
            nenner = x + (-1 * polstelle)
            fkt_gekuerzt = r'~=~ \lim \limits_{x \to ' + str(polstelle) + '} ~ ' + latex(faktor) + \
                           r' \cdot (x' + vorz_str(polstelle) + '~)'
        fkt = r' \frac{' + latex(zaehler) + '}{' + latex(nenner) + '}'
        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n'))]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']
        if a in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + ') Bestimmen Sie den Grenzwert durch Termumformungen.')
            aufgabe.append(r' \lim \limits_{x \to ' + str(polstelle) + '} ~' + fkt)
            loesung.append(str(liste_teilaufg[i]) + r') \quad \lim \limits_{x \to ' + str(polstelle) + '} ~' + fkt +
                           r'~=~ \lim \limits_{x \to ' + str(polstelle) + r'} ~ \frac{' + latex(faktor) + '(x' +
                           vorz_str(polstelle) + r') \cdot (x~' + vorz_str(-1 * polstelle) + ')}{' + latex(nenner) + '}' +
                           fkt_gekuerzt + r'~=~' + str(faktor * (polstelle * 2)) + r'\quad (4P) \\')
            Punkte += 4
            i += 1

        return [aufgabe, loesung, Punkte]


    def aenderungsrate(nr, teilaufg):
        liste_teilaufg = [a, b, c, d]
        i = 0
        Punkte = 0

        faktor = zzahl(1, 20) / 10
        s_xwert = zzahl(1, 3)
        s_ywert = zzahl(1, 3)
        abstand = random.choice([[-1, 2], [-2, 1]])

        x_wert_1 = s_xwert + abstand[0]
        x_wert_2 = s_xwert + abstand[1]
        y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
        y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
        werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

        max_werte = 5.5
        regeln = [lambda _: all(wert < max_werte for wert in werte),
                  lambda _: all(wert > -max_werte for wert in werte)]
        while not all(regel(werte) for regel in regeln):
            s_xwert = zzahl(1, 3)
            s_ywert = zzahl(1, 3)
            abstand = random.choice([[-1, 2], [-2, 1]])

            x_wert_1 = s_xwert + abstand[0]
            x_wert_2 = s_xwert + abstand[1]
            y_wert_1 = faktor * (x_wert_1 - s_xwert) ** 2 + s_ywert
            y_wert_2 = faktor * (x_wert_2 - s_xwert) ** 2 + s_ywert
            werte = [x_wert_1, x_wert_2, y_wert_1, y_wert_2]

        print(f'\033[0;36mIntervall: [X: {x_wert_1} Y: {round(y_wert_1, 2)} | '
              f'X: {x_wert_2} Y: {round(y_wert_2, 2)}]\033[0m')

        fkt = expand(faktor * (x - s_xwert) ** 2 + s_ywert)
        fkt_str = latex(faktor) + 'x^2' + vorz_str(-2 * faktor * s_xwert) + 'x' + vorz_str(
            (faktor * (s_xwert ** 2)) + s_ywert)
        # y_wert_1 = N(fkt.subs(x, x_wert_1), 3) Schien mir unnötig und führte in manchen Fällen zu Fehlern in Verbindung
        # y_wert_2 = N(fkt.subs(x, x_wert_2), 3) mit dem Code weiter oben
        fkt_abl = diff(fkt, x)
        fkt_abl_x0 = fkt_abl.subs(x, x_wert_2)

        print('f(x)=' + str(fkt))
        print('f`(x)=' + str(fkt_abl))
        print('f`(x_0)=' + str(fkt_abl_x0))

        aufgabe = [MediumText(bold('Aufgabe ' + str(nr) + ' \n\n')), 'Gegeben ist die folgende Funktion:',
                   r'f(x)~=~' + fkt_str]
        loesung = [r' \mathbf{Lösung~Aufgabe~}' + str(nr) + r' \hspace{35em}']

        if a in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + f') Bestimme zeichnerisch die mittlere Änderungsrate im Interval '
                                                    f'[ {x_wert_1} | {x_wert_2} ] vom Graphen f. \n\n')

            if y_wert_1 == y_wert_2:
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~m~bestimmt~(1P)} \\')
                Punkte += 2
            else:
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Gerade~durch~beide~Punkte~(1P),~~Steigungsdreieck~(1P)'
                                                        ',~~m~bestimmt~(1P)} \\')
                Punkte += 3

            dy = y_wert_2 - y_wert_1
            dx = x_wert_2 - x_wert_1
            fkt_sekante = dy / dx * (x - x_wert_2) + y_wert_2
            xwerte = [-6 + x / 5 for x in range(60)]
            xwerte_geraden = [-6, 6]
            ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
            Graph(xwerte, ywerte, s_xwert, fkt, 'f', f'{path}Aufgabe_4')

            xwerte_dy = [x_wert_2, x_wert_2]
            ywerte_dy = [y_wert_1, y_wert_2]
            xwerte_dx = [x_wert_1, x_wert_2]
            ywerte_dx = [y_wert_1, y_wert_1]

            ywerte_sekante = [fkt_sekante.subs(x, -6), fkt_sekante.subs(x, 6)]

            plt.plot(xwerte_dy, ywerte_dy)
            plt.plot(xwerte_dx, ywerte_dx)
            plt.plot(xwerte_geraden, ywerte_sekante)

            if c not in liste_teilaufg:
                pass
            plt.savefig(f'{path}loesung_Aufgabe_4', dpi=150)

            i += 1

        if b in teilaufg:
            aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die mittlere Änderungsrate im Interval'
                                                    f' [ {x_wert_1} | {x_wert_2} ] durch Rechnung. \n\n')
            loesung.append(str(liste_teilaufg[i]) + r') \quad \frac{ \Delta y}{ \Delta x} ~=~ \frac{' +
                           latex(N(y_wert_2, 3)) + vorz_str(-1 * N(y_wert_1, 3)) +
                           '}{' + str(x_wert_2) + vorz_str(-1 * x_wert_1) + '} ~=~' +
                           latex(N(Rational(y_wert_2 - y_wert_1, x_wert_2 - x_wert_1), 3)) +
                           r' \quad \to \quad \mathrm{Zeichnung~stimmt~überein} \quad (4P) \\')
            Punkte += 4
            i += 1

            if c in teilaufg:
                aufgabe.append(str(liste_teilaufg[i]) + f') Bestimme zeichnerisch die lokale Änderungsrate an der Stelle x = {x_wert_2}. \n\n')
                loesung.append(str(liste_teilaufg[i]) + r') \quad \mathrm{Tangente~an~Punkt~(1P),~m~bestimmt~(1P)}  \\')
                i += 1

            if a not in teilaufg:
                xwerte = [-6 + x / 5 for x in range(60)]

                ywerte = [fkt.subs(x, xwerte[i]) for i in range(60)]
                Graph(xwerte, ywerte, s_xwert, fkt, 'f', f'{path}Aufgabe_4')

                steigung_tangente = fkt_abl.subs(x, x_wert_2)
                fkt_tangente = steigung_tangente * (x - x_wert_2) + y_wert_2
                ywerte_tangente = [fkt_tangente.subs(x, -6), fkt_tangente.subs(x, 6)]
                plt.plot(xwerte_geraden, ywerte_tangente)
                plt.savefig(f'{path}loesung_Aufgabe_4', dpi=150)

                Punkte += 3
                i += 1

            if d in teilaufg:
                aufgabe.append(str(liste_teilaufg[i]) + f') Überprüfe die lokale Änderungsrate an der Stelle x = {x_wert_2} mit einer Rechnung. \n\n')
                Division_fkt_linear = (fkt - fkt.subs(x, x_wert_2)) / (x - x_wert_2)
                partialbruch = apart(Division_fkt_linear)
                print(Division_fkt_linear)
                print(partialbruch)
                loesung.append(str(liste_teilaufg[i]) + r') \quad \lim \limits_{x \to ' + str(x_wert_2) + r'} ~ \frac{' +
                               fkt_str + vorz_str(N(-1 * fkt.subs(x, x_wert_2), 3)) + '}{x~' + vorz_str(-1 * x_wert_2) + '} ~=~' +
                               r' \lim \limits_{x \to ' + str(x_wert_2) + '}' + latex(partialbruch) + '~=~' +
                               latex(N(fkt_abl_x0, 3)) + r' \quad (3P) \\')
                Punkte += 3

        # plt.show()
        return [aufgabe, loesung, Punkte]

    aufgaben = [folgen(1, [a, b, c, d]), grenzwerte_folgen(2, [a]),
                grenzwerte_funktionen(3, [a]), aenderungsrate(4, [a, b, c, d])]
    Punkte = str(sum(aufgabe[2] for aufgabe in aufgaben))
    # Angaben für den Test im pdf-Dokument
    fach = 'Mathematik'
    datum = datetime.date.today().strftime('%d.%m.%Y')
    try:
        lehrer = lehrer.replace('_', ' ')
        kurs = kurs.replace('_', ' ')
    except AttributeError:
        pass
    art = 'Grenzwerte und Änderungsraten'


    # der Teil in dem die PDF-Datei erzeugt wird
    def Hausaufgabenkontrolle():
        geometry_options = {"tmargin": "0.2in", "lmargin": "1in", "bmargin": "0.4in", "rmargin": "0.7in"}
        Aufgabe = Document(geometry_options=geometry_options)
        # erste Seite
        if klasse is None and kurs is None and lehrer is None:
            with Aufgabe.create(Center()):
                with Aufgabe.create(Tabular('c|c|c|', row_height=1.2)) as table1:
                    table1.add_hline(2, 3)
                    table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Fach:', 'Datum:')
                    table1.add_row(SmallText('mit gymnasialer Oberstufe'), fach, datum)
                    table1.add_hline(2, 3)
            Aufgabe.append(LargeText(bold(f'\n {art} \n\n')))
        else:
            table1 = Tabular('c|c|c|c|c|c|', row_height=1.2)
            table1.add_hline(2, 6)
            table1.add_row(MediumText(bold('Torhorst - Gesamtschule')), 'Klasse:', 'Fach:', 'Niveau:', 'Lehrkraft:',
                           'Datum:')
            table1.add_row(SmallText('mit gymnasialer Oberstufe'), klasse, fach, kurs, lehrer, datum)
            table1.add_hline(2, 6)
            Aufgabe.append(table1)
            Aufgabe.append(' \n\n')
            Aufgabe.append(LargeText(bold(f'\n {art} \n\n')))

        for aufgabe in aufgaben:
            for elements in aufgabe[0]:
                if '~' in elements:
                    with Aufgabe.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(elements)
                else:
                    Aufgabe.append(elements)

        Aufgabe.append('\n\n')
        Aufgabe.append(MediumText(bold(f'Du hast ........ von {Punkte} möglichen Punkten erhalten. \n\n')))

        Aufgabe.append(NewPage())
        Aufgabe.append(LargeText(bold('Bearbeitet von:')))
        Aufgabe.append(' \n\n')
        with Aufgabe.create(Figure(position='h!')) as graph:
            graph.add_image(f'{path}Aufgabe_4.png', width='400px')

        Aufgabe.generate_pdf(f'{path}{art}', clean_tex=true)


    # Erwartungshorizont
    def Erwartungshorizont():
        geometry_options = {"tmargin": "0.4in", "lmargin": "1in", "bmargin": "1in", "rmargin": "1in"}
        Loesung = Document(geometry_options=geometry_options)
        Loesung.append(LargeText(bold(f'Lösung für {art}\n\n')))

        for loesung in aufgaben:
            for loesung in loesung[1]:
                if '~' in loesung:
                    with Loesung.create(Alignat(aligns=2, numbering=False, escape=False)) as agn:
                        agn.append(loesung)
                else:
                    Loesung.append(loesung)
        Loesung.append('\n\n')
        Loesung.append(MediumText(bold(f'insgesamt {Punkte} Punkte')))

        Loesung.append(NewPage())
        with Loesung.create(Figure(position='h!')) as graph:
            graph.add_image(f'{path}loesung_Aufgabe_4.png', width='400px')

        Loesung.generate_pdf(f'{path}{art} - Lsg', clean_tex=true)


    # Druck der Seiten
    Hausaufgabenkontrolle()
    Erwartungshorizont()


if __name__ == '__main__':
    # print(sys.argv)
    # print(*sys.argv[1:-1])
    if len(sys.argv) > 1:
        # Über die Website
        path = f'{'/'.join(os.path.abspath(__file__).split('\\')[:-2])}/{sys.argv[-1]}/erstellt/'
        erstellen(*sys.argv[1:-1])
    else:
        # Über das Ausführen der Datei
        path = f'{'/'.join(os.path.abspath(__file__).split('\\')[:-1])}/erstellt/'  # Pfad, an dem PDF und PNG
        # erstellt werden sollen
        # Standard: In einem Ordner ("erstellt") im Unterordner wo die Python-Datei drinnen ist
        erstellen(klasse=11, kurs='Leistungskurs', lehrer='Herr Herrys')
    print(path)
