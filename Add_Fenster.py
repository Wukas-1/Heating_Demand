#Funktion passt wandflächen an und fensterflächen
#Fenster hat jede Wand und jedes Dach 
import copy
from getFensterWand import getFensterAnteile


def Add_Fenster(Zielobjekt,Baujahr):
    [x_wand,x_dach]=getFensterAnteile(Baujahr)
    
    #Reduziere alle Wände um Faktor und füge Fenster hinzu
    Zielobjekt["windows"]=copy.deepcopy(Zielobjekt["walls"])
    for Counter in range(len(Zielobjekt["walls"])):
        
        Zielobjekt["windows"][Counter]["area"]=Zielobjekt["walls"][Counter]["area"]*x_wand
        Zielobjekt["windows"][Counter]["angle"]=90
        Zielobjekt["walls"][Counter]["area"]=Zielobjekt["walls"][Counter]["area"]*(1-x_wand)
        
        

    
    #Reduziere Dächer um Faktor und füge  Fenster hinzu 
    
    BufferDach=copy.deepcopy(Zielobjekt["roofs"])
    for Counter in range(len(Zielobjekt["roofs"])):
        
        print(Zielobjekt["roofs"][Counter]["area"])
        
        Zielobjekt["roofs"][Counter]["area"]=Zielobjekt["roofs"][Counter]["area"]*(1-x_dach)
        BufferDach[Counter]["area"]=BufferDach[Counter]["area"]*x_dach
        
    
    
    
    Zielobjekt["windows"]= Zielobjekt["windows"] + BufferDach
    
    
    return(Zielobjekt)