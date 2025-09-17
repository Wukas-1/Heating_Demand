#Berechnung der Lüftungswärmesenken

def LueftungsVerluste(Zielobjekt,T_i,T_A,H_V_inf,t,Monate,n_inf,V_N):
    
    #Verluste durch Infiltration
    Q_V_inf=H_V_inf*(T_i-T_A)*t*Monate
    
    #Verluste durch Lüften 
    n_win_delta=0.5-n_inf-0.1
    
    if n_win_delta<0:
        n_win_delta=0
        
    n_win=0.1+n_win_delta*(1)
    
    n_win_mth=n_win*(T_A*0.04+0.08)
    
    H_V_win=n_win_mth*V_N*0.34
    
    Q_V_win=H_V_win*(T_i-T_A)*t*Monate
    
    for Counter in range(12):
        if Q_V_inf[Counter]<0:
            Q_V_inf[Counter]=0
        if Q_V_win[Counter]<0:
            Q_V_win[Counter]<0
 
    
    return(Q_V_inf/1000,Q_V_win/1000,H_V_win)
