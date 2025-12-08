from data import Urg2022_pub,UrgP2022
import numpy as np
import pandas as pd
import statsmodels.api as sm

#Inputs
Medecins2022 = UrgP2022[UrgP2022["PERSO"].isin(["M1000","M2000","M3020"])]
ETP_Medecins2022 = Medecins2022.groupby("FI",as_index=False)["ETPSAL"].sum()

Infirmieres2022 = UrgP2022[UrgP2022["PERSO"].isin(["N2200","N2300"])]
ETP_Infirmieres2022 = Infirmieres2022.groupby("FI",as_index=False)["ETPSAL"].sum()

Aides_soignantes2022 = UrgP2022[UrgP2022["PERSO"].isin(["N2510","N2530"])]
ETP_Aides_soignantes2022 = Aides_soignantes2022.groupby("FI",as_index=False)["ETPSAL"].sum()

Admin2022 = UrgP2022[UrgP2022["PERSO"].isin(["N1210"])]
ETP_Admin2022 = Admin2022.groupby("FI",as_index=False)["ETPSAL"].sum()

#Outputs
Passages = Urg2022_pub[["FI","PASSU"]]

##Estimation pour les établissements publics
#Passage des données en log
Passages["PASSU"] = Passages["PASSU"].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)
ETP_Medecins2022["ETPSAL"] = ETP_Medecins2022["ETPSAL"].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)
ETP_Infirmieres2022["ETPSAL"] = ETP_Infirmieres2022["ETPSAL"].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)
ETP_Aides_soignantes2022["ETPSAL"] = ETP_Aides_soignantes2022["ETPSAL"].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)
ETP_Admin2022["ETPSAL"] = ETP_Aides_soignantes2022["ETPSAL"].apply(lambda x: np.log(x) if pd.notnull(x) and x > 0 else 0)

#Fusion en un seul dataframe, en regroupant par le finess
df = Passages.merge(ETP_Medecins2022, on="FI", how="left", suffixes=("", "_med"))
df = df.merge(ETP_Infirmieres2022, on="FI", how="left", suffixes=("", "_inf"))
df = df.merge(ETP_Aides_soignantes2022, on="FI", how="left", suffixes=("", "_as"))
df = df.merge(ETP_Admin2022, on="FI", how="left", suffixes=("", "_adm"))
df = df.rename(columns={"ETPSAL": "ETP_med","ETPSAL_inf": "ETP_inf","ETPSAL_as":  "ETP_as","ETPSAL_adm": "ETP_adm"})

df = df.fillna(0)


X = df[["ETP_med", "ETP_inf", "ETP_as", "ETP_adm"]]
X = sm.add_constant(X)
Y = df["PASSU"]

model = sm.OLS(Y, X).fit()
print(model.summary())
