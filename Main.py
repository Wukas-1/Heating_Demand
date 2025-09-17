#Berechnung des Heizenergiebedarfs nach DIN V 18599

import numpy as np
from getStrahlung import getStrahlung
from Geometrie import Geometrie
from Add_Fenster import Add_Fenster
from BilanzinnnenTemperatur import BilanzinneTemperatur
from Transmission import Transmissionswaermesenken
from LueftungsVerluste import LueftungsVerluste
from SenkenOpak import SenkenOpak
from FensterGewinne import FensterGewinne
from InterneGewinne import InterneGewinne
from Ausnutzungsgrad import Ausnutzungsgrad
import matplotlib.pyplot as plt
import json

#Lade City GML Daten-----------------------------------------------------------
with open("Lindenstrasse15.json", encoding="utf-16") as file:
    file_content = file.read()
    data = json.loads(file_content)
    
    
    
    
#Suche Addresse in data, kann später entfernt werden---------------------------

Zieladresse="Lindenstrasse 7, Regensburg"

for Gebäude in data:
    
    Buffer=data[Gebäude]
    if Buffer["address"] == Zieladresse:
        Zielobjekt=data[Gebäude]
        break
    
Baujahr=1990
Sanierung_all=0
Sanierung_Fenster=0
Sanierung_Dach=0
Sanierung_Wand=0
Sanierung_Boden=0
flag_maggie=1
#Fenster 500 m^2
#Wand 200 m^2

#Ende input Parameter 
    
#Definition fixer Parameter, sollen aber auch vom Benutzer angepasst werden um Nutzungsverhalten zu verbessern
T_Soll=20#Soll Innentemperatur [°C]
t_na=7#Dauer der Nachtabsenkung [h]
T_na=4#Nachtabsenkung um 4K
t=24#Dauer des Berechnungsschrittes [h]
T_A=np.array([-1.2, 0.4, 4.3, 8.2, 13.7, 16.4, 18, 17.8, 13.1, 8.7, 3, -0.2 ])# Außentemperatur der Referenzstadt Passau[°C]
Monate=np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]);#Anzahl der Tage pro Monat, kein Schaltjahr
#Ende Eingangsdaten------------------------------------------------------------

#Berechnung Nutzfläche und Nettovolumen
[A_N,V_N,A_E]=Geometrie(Zielobjekt)

#Anpassung der Wandflächen un hinzufügen von Fensterflächen
Zielobjekt=Add_Fenster(Zielobjekt,Baujahr)

#Berechne die Strahlung für alle Bauteile
Zielobjekt=getStrahlung(Zielobjekt)

#Berechnung der Bilanzinnentemperatur
[T_i,T_2,T_1,H_T_H,H_T_B,H_V_inf, n_inf, U_Wand, U_Dach,tau,g]=BilanzinneTemperatur(Zielobjekt, T_A, T_Soll, t_na, T_na, A_N, V_N, A_E,Baujahr,Sanierung_all,Sanierung_Fenster,Sanierung_Dach,Sanierung_Wand,Sanierung_Boden,flag_maggie)

#Berechnung der Transmissionswärmesenken
[Q_TH,Q_TB]=Transmissionswaermesenken(Zielobjekt, H_T_H, H_T_B, T_i, T_A,Monate,t)

#Berechnung der Lüftungswärmesenken
[Q_V_inf,Q_V_win,H_V_win]=LueftungsVerluste(Zielobjekt, T_i, T_A, H_V_inf, t, Monate, n_inf, V_N)

#Berechnung der Senken opaker Bauteile und Gewinne opaker Bauteil
[Q_V_opak,Q_S_opak]=SenkenOpak(Zielobjekt, U_Wand, U_Dach, t, Monate)

#Berechnung der Gewinne durch Fenster 
Q_S_opak_win=FensterGewinne(Zielobjekt,Baujahr,t,Monate,g)

#Berechnung der Internen Gewinne
Q_S_intern=InterneGewinne(A_N,Monate)

#Bildung der Summen
Q_Verluste=Q_TH+Q_TB+Q_V_inf+Q_V_win+Q_V_opak
Q_Gewinne=Q_S_opak+Q_S_opak_win+Q_S_intern

#Berechhnung des Ausnutzungsgrad der Wärmequellen
n=Ausnutzungsgrad(Q_Gewinne, Q_Verluste, tau)

#Bilden der Gesamtbilanz
Q_H=Q_Verluste-n*(Q_Gewinne)

#Normieren auf die Nutzfläche

Q_H=Q_H/A_N

End=np.nansum(Q_H)+12.5

#Visualisierung Endergebnisse

bars = ('Januar', 'Februar', 'März', 'April', 'Mai','Juni','Juli','August','September','Oktober','November','Dezember')


# Create bars
plt.bar(bars,Q_H)
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels by 45 degrees and align to the right
plt.xticks(fontsize=10, fontname='Arial',fontweight='bold')
plt.yticks(fontsize=10, fontname='Arial',fontweight='bold')
plt.ylabel('Heizendenergiebedarf [kWh/m^2*a]', fontname='Arial',fontweight='bold')



