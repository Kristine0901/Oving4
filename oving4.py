import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Oppgave 4
df = pd.read_csv("Oving4/load_data.csv", decimal=",")

# Gjør indeksen om til DatetimeIndex
df.columns = df.columns.str.strip()
df["Time(Local)"] = pd.to_datetime(df["Time(Local)"],dayfirst = True, utc=True)
df = df.set_index("Time(Local)")
df = df.sort_index()
df = df.tz_convert("Europe/Oslo")

print(df.head())

# Oppgave 5
print(df.index[0])

#oppgave 6
df6 = df.loc["2026-01-01 03:00:00 +01:00"]
df6.plot(kind= "bar", figsize=(10,5))
plt.title("Produksjon og consumption 01.01.2026 kl 03:00:00")
plt.grid(True)

plt.savefig("Oving4/Observasjonkl0300.png")

plt.show()

df61 = df.loc["2026-01-01 00:00:00 +01:00": "2026-01-01 23:00:00 +01:00"]
df61.plot(figsize=(10,5))
plt.title("Produksjon og consumption 01.01.2026 kl 00:00 til kl 23:00 +01:00")
plt.grid(True)

plt.savefig("Oving4/ObservasjonEnLastProfil.png")

plt.show()

#oppgave 7
df["Netto"] = (df["Production"] - df["Consumption"])
print(df["Netto"])

#Oppgave 8
tid_max = df["Production"].idxmax()
df_max = df["Production"].max()

print( "Max:",tid_max, df_max)

tid_min = df["Production"].idxmin()
df_min = df["Production"].min()

print("Min:",tid_min, df_min)

df_mean = df["Production"].mean()
print("Gjennomsnittlig produksjon: ", round(df_mean, 2))

#Oppgave 9
tid_Netto_max = df["Netto"].idxmax()
df_Netto_max = df["Netto"].max()

print( "Netto Max:",tid_Netto_max, round(df_Netto_max,2))

tid_Netto_min = df["Netto"].idxmin()
df_Netto_min = df["Netto"].min()

print("Netto Min:",tid_Netto_min, round(df_Netto_min,2))

#Oppgave 10
df_total_produksjon = df["Production"].sum()
print("Total produksjon: ", df_total_produksjon)
