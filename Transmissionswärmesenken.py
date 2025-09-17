def Transmissionswaermesenken(Zielobjekt,H_T_H,H_T_B,T_i,T_A,Monate,t):
    
    Q_TH=H_T_H*(T_i-T_A)*t*Monate#Verluste Wand/Dach/Fenster
    
    #Temperatur des Unbeheizten Kellers
    T_UB=T_i-0.8*(T_i-T_A)
    
    Q_TB=H_T_B*(T_i-T_UB)*t*Monate
    
    #Entferne negative Elemente müssen im Kühlbedarf bilanziert werden nicht im Wärmebedarf
    
    for Counter in range(12):
        if Q_TB[Counter]<0:
            Q_TB[Counter]=0
        if Q_TH[Counter]<0:
            Q_TH[Counter]<0
        
    
    return(Q_TH/1000,Q_TB/1000)#Umwandlung in kWh
