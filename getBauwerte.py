def getBauwerte(Baujahr,Sanierung_all,Sanierung_Fenster,Sanierung_Dach,Sanierung_Wand,Sanierung_Boden,flag_maggie):
    
    
    
    if Baujahr <= 1918:
        U_Wand=1.3
        U_Dach=2.6
        U_Boden=1.6
        U_Fenster=3
        g=0.78
    
    if Baujahr>1918 and Baujahr<=1948:
        U_Wand=1.3
        U_Dach=1.4
        U_Boden=1.6
        U_Fenster=3
        g=0.78
    
    if Baujahr>1948 and Baujahr <=1957:
        U_Wand=1.3
        U_Dach=1.4
        U_Boden=2.3
        U_Fenster=3
        g=0.78
    
    if Baujahr>1957 and Baujahr<=1968:
        U_Wand=1.4
        U_Dach=1.4
        U_Boden=1.0
        U_Fenster=3
        g=0.78
        
    if Baujahr>1968 and Baujahr<=1978:
        U_Wand=1.0
        U_Dach=0.8
        U_Boden=1.0
        U_Fenster=3
        g=0.78
    
    if Baujahr>1978 and Baujahr<=1983:
        U_Wand=0.8
        U_Dach=0.7
        U_Boden=0.8
        U_Fenster=3
        g=0.78
    
    if Baujahr>1983 and Baujahr<=1994:
        U_Wand=0.6
        U_Dach=0.5
        U_Boden=0.6
        U_Fenster=3
        g=0.78
        
    if Baujahr>1994 and Baujahr<2001:
        U_Wand=0.5
        U_Dach=0.3
        U_Boden=0.6
        U_Fenster=1.9
        g=0.78
        
    if Baujahr>2001 and Baujahr<=2009:
        U_Wand=0.45
        U_Dach=0.3
        U_Boden=0.4
        U_Fenster=1.7
        g=0.78
        
    if Baujahr>2009:
        U_Wand=0.24
        U_Dach=0.24
        U_Boden=0.3
        U_Fenster=1.3
        g=0.78
      
    #Sanierungsmaßnahmen     
    if Sanierung_all==1:
        U_Wand=0.2
        U_Dach=0.2
        U_Boden=0.25
        U_Fenster=0.95
        g=0.7
    if Sanierung_Fenster==1:
        U_Fenster=0.95
        g=0.78
    if Sanierung_Boden==1:
        U_Boden=0.25
    if Sanierung_Dach==1:
        U_Dach=0.2
    if Sanierung_Wand==1:
        U_Wand=0.2
        
    #Bauwerte vom Maggie Gebäude für Validierung   
    if flag_maggie==1:
        U_Wand=0.2
        U_Dach=0.2
        U_Fenster=0.8
        U_Boden=0.23
        g=0.7
        
        
        
        

    return(U_Fenster,U_Dach,U_Boden,U_Wand,g)