import numpy as np
def SenkenOpak(Zielobjekt,U_Wand,U_Dach,t,Monate):
    
    
    #Aller Wände---------------------------------------------------------------
    Q_V_Wand=0
    for Wand in Zielobjekt["walls"]:
        Q_V_Wand=0.04*U_Wand*Wand["area"]*(0.5*4.5*10-0.4*Wand["Strahlung"])*t*Monate+Q_V_Wand
    
    Q_V_Wand=Q_V_Wand.astype(float)    
    
    #Aller Dächer--------------------------------------------------------------
    Q_V_Dach=0
    for Dach in Zielobjekt["roofs"]:
        if Dach["angle"]<45:
            F_F=1
        else:
            F_F=0.5
        
        Q_V_Dach=0.04*U_Dach*Dach["area"]*(F_F*4.5*10-0.6*Dach["Strahlung"])*t*Monate+Q_V_Dach
    
    Q_V_Dach=Q_V_Dach.astype(float)    
    
    Q_S_Dach=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=np.float32)
    Q_S_Wand=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],dtype=np.float32)
    
    for Monat in range(12):
        
        if Q_V_Wand[Monat]<0:
            Q_S_Wand[Monat]=Q_V_Wand[Monat]*(-1)
            Q_V_Wand[Monat]=0
        
        if Q_V_Dach[Monat]<0:
            Q_S_Dach[Monat]=Q_V_Dach[Monat]*(-1)
            Q_V_Dach[Monat]=0
    
    
        

    Q_V_opak=Q_V_Wand+Q_V_Dach
    Q_S_opak=Q_S_Wand+Q_S_Dach
    return(Q_V_opak/1000,Q_S_opak/1000)
        
