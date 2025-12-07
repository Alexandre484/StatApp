import numpy as np
import pandas as pd

MCO2022 = pd.read_csv("SAE/2022/MCO_2022r.csv", sep=";", encoding="latin-1")
Urg2022 = pd.read_csv("SAE/2022/URGENCES_2022r.csv", sep=";", encoding="latin-1")
Q202022 = pd.read_csv("SAE/2022/Q20_2022r.csv", sep=";", encoding="latin-1")

FINESS = pd.read_excel("finess.xlsx")
print(FINESS)