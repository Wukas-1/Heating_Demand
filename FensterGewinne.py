
import numpy as np
def FensterGewinne(Zielobjekt,Baujahr,t,Monat,g):
    
    g_tot=g
    
    g_eff=0.9*0.9*1*g_tot
    
    
    Q_S_opak_windows=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    
    for Fenster in Zielobjekt["windows"]:
        Q_S_opak_windows=Q_S_opak_windows+0.7*Fenster["area"]*g_eff*Fenster["Strahlung"]*t*Monat
    
    Q_S_opak_windows=Q_S_opak_windows.astype(float)
    return(Q_S_opak_windows/1000)
    