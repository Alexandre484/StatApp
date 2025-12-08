import pandas as pd

#importation des données sous forme de dataframes
MCO2022 = pd.read_csv("SAE/2022/MCO_2022r.csv", sep=";", encoding="latin-1")
Urg2022 = pd.read_csv("SAE/2022/URGENCES2_2022r.csv", sep=";", encoding="latin-1")
SSR2022 = pd.read_csv("SAE/2022/SSR_2022r.csv", sep=";", encoding="latin-1")

UrgP2022 = pd.read_csv("SAE/2022/URGENCES_P_2022a.csv", sep=";",encoding="latin-1")

#Q202022 = pd.read_csv("SAE/2022/Q20_2022r.csv", sep=";", encoding="latin-1")

FINESS = pd.read_excel("finess.xlsx")
FINESS = FINESS.drop(FINESS.columns[[1,2,4]],axis=1)
FINESS = FINESS.rename(columns={"FINESS":"FI","Statut Juridique":"Statut"})

#ajout d'une colonne aux données indiuant le statut de chaque établissement
MCO2022 = MCO2022.merge(FINESS,on='FI',how='left')
Urg2022 = Urg2022.merge(FINESS, on='FI', how='left')
SSR2022 = SSR2022.merge(FINESS, on='FI', how='left')

#Separation établissements publics et privés dans des tables distinctes
MCO2022_pub = MCO2022[MCO2022["Statut"] == "Public"]
#MCO2022_priv = MCO2022[MCO2022["Statut"] == "Privé lucratif" or MCO2022["Statut"] == "Privé non lucratif"]

Urg2022_pub = Urg2022[Urg2022["Statut"] == "Public"]
#Urg2022_priv = Urg2022[Urg2022["Statut"] == "Privé lucratif" or Urg2022["Statut"]=="Privé non lucratif"]

