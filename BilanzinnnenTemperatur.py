import math
import numpy as np
from getBauwerte import getBauwerte
def BilanzinneTemperatur(Zielobjekt, T_A, T_soll, t_na, T_na, A_N,V_N,A_E,Baujahr,Sanierung_all,Sanierung_Fenster,Sanierung_Dach,Sanierung_Wand,Sanierung_Boden,flag_maggie):

    # Viele einzel größen müssen bestimmt werden
    # bevor die Bilanzinnentemperatur ausgerechnet werden kann

    # Berechnung der Wirksamen Wärmekapazität der Gebäudezone
    C_wirk = A_N*50  # [Wh/K]

    # Berechnung der Transmissionswärmekoeffizienten----------------------------

    H_T_H = 0  # Transmissionswärmekoeffiziente Wand/Dach/Fenster
    H_T_B = 0  # Transmissionswärmekoeffiziente Boden


    #Durch get Funktion ersetzen
    [U_Fenster,U_Dach,U_Boden,U_Wand,g]=getBauwerte(Baujahr,Sanierung_all,Sanierung_Fenster,Sanierung_Dach,Sanierung_Wand,Sanierung_Boden,flag_maggie)
    
    
    #Berechnung Transmissionswärmekoeffiziente Wand/Dach/Fenster
    for Fenster in Zielobjekt["windows"]:
        H_T_H=H_T_H+U_Fenster*Fenster["area"]+Fenster["area"]*0.1
    for Wände in Zielobjekt["walls"]:
        H_T_H=H_T_H+U_Wand*Wände["area"]+Wände["area"]*0.1
    for Dach in Zielobjekt["roofs"]:
        H_T_H=H_T_H+U_Dach*Dach["area"]+Dach["area"]*0.1
        
    #Berechnung Transmissionswärmekoeffiziente Wand/Dach/Fenster
    for Boden in Zielobjekt["grounds"]:
        H_T_B=H_T_B+U_Boden*Boden["area"]



    #Berechnung der Wärmetransferkoeffizient Infiltration
    if Zielobjekt["volume"]<=1500:#Annahme Gebäudeklasse 1 
        n_50=6
    else:
        n_50=(9*A_E)/V_N
        
    n_inf=n_50*0.07*1
    
    H_V_inf=n_inf*V_N*0.34
    
    #Berechnung der Wärmetransferkoeffizient Lüftung
    #Normalerweise sasonale Berücksichtigung bei der Lüftung, allerding wird mittelwert gebildet bei der Berechnung
    #Bei der Bilanzierung der Lüftungsverluste wird mit Monatswerten gerechnet
    n_win_delta=0.5-n_inf-0.1
    if n_win_delta<0:
        n_win_delta=0
        
    n_win=0.1+n_win_delta*(1)
    
    n_win_mth=n_win*(8.6*0.04+0.08)
    
    H_V_win=n_win_mth*V_N*0.34
    
    #Berechnung der Zeitkonstante
    
    tau=C_wirk/(H_T_H+0.5*H_T_B+H_V_inf+H_V_win)
    
    #Korrekturfaktor der Nachtabsenkung
    f_na=0.13*(7/24)*math.exp((-tau)/250)
    
    T_1=T_soll-4*(7/24)
    
    T_2=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
    T_2=T_soll-f_na*(T_soll-T_A)
    
    T_i=np.array([1,1,1,1,1,1,1,1,1,1,1,1],dtype=np.float64)
    
    for Months in range(12):
         if T_1<T_2[Months]:
             T_i[Months]=T_2[Months]
         else:
             T_i[Months]=T_1
             
    return(T_i,T_2,T_1,H_T_H,H_T_B,H_V_inf,n_inf,U_Wand,U_Dach,tau,g)
    
    
    
    
    
    
    
    
    
    
    
    
    