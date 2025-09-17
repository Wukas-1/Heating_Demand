def Ausnutzungsgrad(Q_Gewinne,Q_Verluste,tau):
    
    
    
    a=1+tau/16
    
    y=Q_Gewinne/Q_Verluste
    
    n=(1-y**a)/(1-y**(a+1))
    
    return(n)