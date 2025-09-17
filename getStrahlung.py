import pandas as pd
def getStrahlung(Zielobjekt):
    
    Strahlung=pd.read_excel('Strahlung_data.xlsx')
    Strahlung=Strahlung.fillna(method="ffill")


    Counter = 0
    for Wand in Zielobjekt["walls"]:
        direction = Wand["direction"]
        filtered_Strahlung = Strahlung[(Strahlung['Orientierung'] == direction) & (Strahlung['Neigung'] == '90°')]
        Strahlung_values = filtered_Strahlung.values.flatten()[2:]
        Zielobjekt["walls"][Counter]["Strahlung"] = Strahlung_values
        Counter += 1

    Counter = 0
    for Dach in Zielobjekt["roofs"]:
        Winkel= min([0, 30, 45, 60, 90], key=lambda x: abs(x -(Dach["angle"])))
        Winkel=str(Winkel)+'°'
        direction = Dach["direction"]
        filtered_Strahlung = Strahlung[(Strahlung['Orientierung'] == direction) & (Strahlung['Neigung'] == Winkel)]
        Strahlung_values = filtered_Strahlung.values.flatten()[2:]
        Zielobjekt["roofs"][Counter]["Strahlung"] = Strahlung_values
        Counter += 1

    Counter = 0
    for Fenster in Zielobjekt["windows"]:
        Winkel= min([0, 30, 45, 60, 90], key=lambda x: abs(x -( Fenster["angle"])))
        Winkel=str(Winkel)+'°'
        direction = Fenster["direction"]
        filtered_Strahlung = Strahlung[(Strahlung['Orientierung'] == direction) & (Strahlung['Neigung'] == Winkel)]
        Strahlung_values = filtered_Strahlung.values.flatten()[2:]
        Zielobjekt["windows"][Counter]["Strahlung"] = Strahlung_values
        Counter += 1
        
    return(Zielobjekt)