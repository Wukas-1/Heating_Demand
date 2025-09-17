def Geometrie(Zielobjekt):
    
    
    Anzahl_Geschosse=round(Zielobjekt["heightWithoutRoof"]/3)
    
    A_N=0.32*Zielobjekt["volume"]#Nutzfläche
    
    #Nettoraumvolumen in Abhängigkeit der Geschosse
    if Anzahl_Geschosse<=3:
        V_N=0.76*Zielobjekt["volume"]
    else:
        V_N=0.8*Zielobjekt["volume"]
               

    #Berechnung der Hüllfläche
    A_E=0
    for Element in Zielobjekt["walls"]:
        A_E=A_E+Element["area"]
    for Element in Zielobjekt["roofs"]:
        A_E=A_E+Element["area"]
    for Element in Zielobjekt["grounds"]:
        A_E=A_E+Element["area"]
        

    return(A_N,V_N,A_E)
